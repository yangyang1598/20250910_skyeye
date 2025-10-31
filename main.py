import sys
import os
import json
from datetime import datetime,timedelta,timezone
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QSpacerItem, QSizePolicy, QMessageBox, QInputDialog
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QTimer, QObject, Slot
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebChannel import QWebChannel

# 위젯 모듈 임포트
from widget.camera_md_data_widget import CameraMdDataWidget
import widget.camera_md_data_widget as camera_md_data_widget_module
from widget.camera_control_widget import CameraControlWidget
from widget.bottom_widget import BottomWidget
from widget.fire_sensor_widget import FireSenSorWidget
from widget.ir_camera_set_widget import IRCameraSetWidget
from dialog.mission_device_list_dialog import MissionDeviceListDialog
from protocol import Protocol
import protocol as protocol_module
from db.db_poi import Poi


isIR=False 

# ------------------------------
# WebChannel 핸들러
# ------------------------------
class WebChannelHandler(QObject):
    """JavaScript ↔ Python 통신 핸들러"""

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
    
    # --------------------------
    # 데이터 표기
    # --------------------------
    @Slot('QVariant')
    def showCameraDialog(self, data):
        """JavaScript → Python: 카메라 다이얼로그 호출"""
        try:
            if isinstance(data, str):
                data = json.loads(data)
            elif hasattr(data, 'toVariant'):
                data = data.toVariant()

            # print(f"📷 카메라 다이얼로그 데이터 수신: {type(data)}")
            self.main_window.show_camera_md_data_widget(data)
            self.main_window.show_camera_control_widget()
            if isIR:
                self.main_window.show_ir_camera_set_widget()
            self.main_window.show_bottom_widget(False)

        except Exception as e:
            print(f"❌ 카메라 다이얼로그 표시 오류: {e}")
            import traceback
            traceback.print_exc()
    # --------------------------
    # 마우스 커서 위치 업데이트
    # --------------------------
    @Slot(float, float)
    def updateCursorLatLng(self, lat, lng):
        """JavaScript → Python: 마우스 커서 위젯 위치 업데이트"""
        self.main_window.update_cursor_latlng(lat, lng)
    # --------------------------
    # 마커 관련
    # --------------------------
    @Slot(float, float)
    def requestMarkerInputs(self, lat, lng):
        """JavaScript → Python: Qt 다이얼로그로 각도/줌 입력 요청"""
        try:
            degree = self.main_window.show_tagert_angle_message()
            if degree is None:
                print("사용자 각도 입력 취소")
                return
            zoom = self.main_window.show_tagert_zoom_message()
            if zoom is None:
                print("사용자 줌 입력 취소")
                return

            # 저장 후 JS에 마커 생성 요청
            self.main_window.set_marker_inputs(degree, zoom, lat, lng)
            js = f"if (typeof addMarkerAt === 'function') {{ addMarkerAt({lat}, {lng}); }}"
            self.main_window.web_view.page().runJavaScript(js)

            print(f"마커 생성 요청: lat={lat}, lng={lng}, degree={degree}, zoom={zoom},site_id={protocol_module.SITE_ID}")
            self.main_window.insert_poi_db(lat,lng,degree,zoom,protocol_module.SITE_ID)
        except Exception as e:
            print(f"❌ 입력 다이얼로그 처리 오류: {e}")

    @Slot(int)
    def requestEditMarkerInputs(self, poi_id: int):
        """JavaScript → Python: POI 마커 편집(각도/줌) 입력 요청
        - 기본값은 DB의 altitude(각도), zoom_level(줌) 사용
        - 대상 좌표는 해당 POI의 latitude/longitude
        """
        try:
            target = None
            poi_list = getattr(self.main_window, 'db_poi_list', []) or []
            for p in poi_list:
                if getattr(p, 'poi_id', None) == poi_id:
                    target = p
                    break

            if not target:
                print(f"POI 편집 대상 없음: poi_id={poi_id}")
                return

            # 편집 기본값으로 설정
            self.main_window.point_degree = target.altitude
            self.main_window.point_zoom = target.zoom_level

            degree = self.main_window.show_tagert_angle_message()
            if degree is None:
                print("사용자 각도 입력 취소")
                return
            zoom = self.main_window.show_tagert_zoom_message()
            if zoom is None:
                print("사용자 줌 입력 취소")
                return

            # 저장: 각도/줌 + 좌표를 MapApp에 반영
            self.main_window.set_marker_inputs(degree, zoom, target.latitude, target.longitude)
            print(f"POI 편집 완료: poi_id={poi_id}, lat={target.latitude}, lng={target.longitude}, degree={degree}, zoom={zoom}")
            self.main_window.update_poi_db(target.latitude,target.longitude,degree,zoom,protocol_module.SITE_ID,poi_id)
        except Exception as e:
            print(f"❌ POI 편집 처리 오류: {e}")
    @Slot()
    def deleteAllMarkers(self):
        """JavaScript → Python: 모든 마커 삭제"""
        try:
            self.main_window.delete_all_markers()
            print("모든 마커 삭제 완료")
        except Exception as e:
            print(f"❌ 모든 마커 삭제 오류: {e}")
    @Slot(int)
    def deleteMarker(self, poi_id: int):
        """JavaScript → Python: 특정 마커 삭제"""
        try:
            self.main_window.delete_marker(poi_id)
            print(f"마커 삭제 완료: poi_id={poi_id}")
        except Exception as e:
            print(f"❌ 마커 삭제 오류: {e}")
            
    # --------------------------
    # 산불 센서 알림 클릭릭
    # --------------------------

    @Slot(int, float, float)
    def onFireSensorClick(self, idx, lat, lng):
        """JavaScript → Python: 산불센서 원 클릭 인덱스 및 좌표 출력"""
        # print(f"🔥 FireSensor 클릭: index={idx}, lat={lat}, lng={lng}")
        # fire sensor 위젯 표시 (카메라 두 위젯은 자동 숨김)
        self.main_window.fire_sensor_widget.set_fire_sensor(index=idx)
        self.main_window.show_fire_sensor_widget(idx)

   
# ------------------------------
# 메인 윈도우 클래스
# ------------------------------
class MapApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.device_data = None
        self.right_container = None
        self.right_layout = None
        self.no_device_message_shown = False
        self.no_data_message_shown = False
        self.prvious_sensor_index=None # 산불감지 송출 인덱스 저장
        self.previous_gas_index=None # 산불감지 변화 저장
        self.previous_flags_index=None # 산불감지 변화 저장

        # 사용자 입력 저장 변수 (map.html로부터 전달)
        self.point_degree = None
        self.point_zoom = None
        self.point_lat = None
        self.point_lng = None

        #DB 클래스 정의
        self.db_poi=Poi()

        # bottom_widget 토글 상태 및 연결/안내 제어 플래그
        self.bottom_toggle_state = False
        self._bottom_move_connected = False
        self.bottom_widget_alert_shown = False
        
        self.init_widget()
        self.setup_ui()
        self.setup_web_channel()
        self.setup_timer()
        
        self.load_map()
        self.setup_window()
        self.setup_mission_device_list()


    # --------------------------
    # 초기화 관련 메서드
    # --------------------------
    def init_widget(self):
        self.camera_md_data_widget = None
        self.camera_control_widget = None
        self.ir_camera_set_widget = IRCameraSetWidget()

        self.bottom_widget = BottomWidget()
        self.protocol = Protocol()
        self.fire_sensor_widget = FireSenSorWidget()

    def setup_ui(self):
        """메인 UI 설정"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.web_view = QWebEngineView()
        self.web_view.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

        self.main_layout = QGridLayout()
        # self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.web_view, 0, 0)
        self.main_layout.setColumnStretch(0, 10)
        self.main_layout.setColumnStretch(1, 0)

        self.main_layout.setRowStretch(0, 10)
        self.main_layout.setRowStretch(1, 0)

        central_widget.setLayout(self.main_layout)

    def setup_web_channel(self):
        """QWebChannel 설정 (JavaScript ↔ Python 통신)"""
        self.channel = QWebChannel()
        self.handler = WebChannelHandler(self)
        self.channel.registerObject("pyHandler", self.handler)
        self.web_view.page().setWebChannel(self.channel)

        
    def setup_timer(self):
        """주기적 데이터 갱신 타이머 설정"""
        self.md_data_timer = QTimer()
        self.md_data_timer.timeout.connect(self.update_device_data)
        self.md_data_timer.start(2000)  # 2초마다 업데이트

        self.sensor_status = QTimer()
        self.sensor_status.timeout.connect(self.update_fire_sensor_circles)
        self.sensor_status.start(2000)  # 2초마다 업데이트

    def setup_window(self):
        """윈도우 속성 설정"""
        self.setWindowTitle("SkyEye Map Application")
        # self.setGeometry(0, 0, 1000, 800) #화면 사이즈 수동 설정
        self.showMaximized() # 화면 최대화
        self.show()

    def load_map(self):
        """HTML 지도 로드"""
        path = os.path.abspath("map.html")
        self.web_view.load(QUrl.fromLocalFile(path))
        self.web_view.loadFinished.connect(self.on_load_finished)

    def setup_sse_event(self):
        # 핸들러 등록: handle_sse_event 메서드를 protocol의 self.sse_event_handler로 등록
        #  sse_event_handler 값이 등록되는 경우 해당 함수 자동 호출
        self.protocol.set_sse_event_handler(self.handle_sse_event)

        # 스트림 연결 시작
        self.protocol.open_sse_stream()
        self.text = {
            "cmd": "connect",
            "mode": "",
            "value": ""
        }
        self.protocol.post_event_message(self.text)
    def setup_mission_device_list(self):
        """미션 디바이스 목록 다이얼로그 설정"""
        data=self.protocol.get_mission_device_list()
        
        self.mission_device_list_dialog = MissionDeviceListDialog(data)
        # 선택/취소 결과 연결
        self.mission_device_list_dialog.accepted.connect(self.on_device_dialog_accepted)
        self.mission_device_list_dialog.rejected.connect(self.on_device_dialog_rejected)
        self.mission_device_list_dialog.show()
    # --------------------------
    # 우측 위젯 표시 관련
    # --------------------------
    def ensure_right_container(self):
        """오른쪽 컨테이너(레이아웃)가 없으면 생성"""
        if not self.right_container:
            self.right_container = QWidget()
            self.right_layout = QVBoxLayout(self.right_container)
            self.right_layout.setContentsMargins(0, 0, 0, 0)
            self.main_layout.addWidget(self.right_container, 0, 1)

    def show_camera_md_data_widget(self, data):
        """카메라 메타데이터 위젯 표시"""
        print(f"카메라 위젯 표시 - 데이터: {data}")
        self.ensure_right_container()

        self.hide_fire_sensor_widget()
        if self.hide_camera_md_data_widget():
            return

        if not self.camera_md_data_widget:
            self.camera_md_data_widget = CameraMdDataWidget()
            self.right_layout.addWidget(self.camera_md_data_widget)

            # 위젯 간의 간격 추가(spacer)
            self.horizontalSpacer = QSpacerItem(10, 60, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
            self.right_layout.addItem(self.horizontalSpacer)

        try:
            self.camera_md_data_widget.update_data(data,isIR)
        except Exception as e:
            print(f"⚠️ 카메라 데이터 업데이트 오류: {e}")

        # 카메라 메타 데이터 위젯 표시
        self.camera_md_data_widget.show()

    def show_camera_control_widget(self):
        """카메라 제어 위젯 표시"""
        self.ensure_right_container()

        self.hide_fire_sensor_widget()
        if self.hide_camera_control_widget():
            return

        if not self.camera_control_widget:
            self.camera_control_widget = CameraControlWidget()
            self.right_layout.addWidget(self.camera_control_widget)

        # 카메라 제어 위젯 표시
        self.camera_control_widget.show()
    
    def show_fire_sensor_widget(self,idx=None):
        """fire sensor 위젯 표시 (카메라 두 위젯은 숨김)"""
        self.ensure_right_container()
    
        if self.fire_sensor_widget.parent() is None:
            self.right_layout.addWidget(self.fire_sensor_widget)
        
        #산불 센서 위젯 송출 시 하단 바 숨김
        self.bottom_widget.hide()
        self.bottom_toggle_state=False

        self.hide_camera_md_data_widget()
        self.hide_camera_control_widget()

        if self.hide_fire_sensor_widget():
            if idx !=self.previous_sensor_index:
               pass
            else:
                return
        self.previous_sensor_index=idx
        self.fire_sensor_widget.show()

    def show_ir_camera_set_widget(self):
        """IR 카메라 설정 위젯 표시"""
        self.ensure_right_container()

        self.hide_fire_sensor_widget()
        if self.hide_ir_camera_set_widget():
            return

        if self.ir_camera_set_widget.parent() is None:
            self.right_layout.addWidget(self.ir_camera_set_widget)
        
        self.ir_camera_set_widget.show()


    def hide_fire_sensor_widget(self):
        """fire sensor 위젯 숨김"""
        if self.fire_sensor_widget and self.fire_sensor_widget.isVisible():
            self.fire_sensor_widget.hide()
            return True
        else:
            return False

    def hide_camera_md_data_widget(self):
        """카메라 데이터 위젯 숨김"""
        if self.camera_md_data_widget and self.camera_md_data_widget.isVisible():
            self.camera_md_data_widget.hide()
            return True
        else:
            return False

    def hide_camera_control_widget(self):
        """카메라 제어 위젯 숨김"""
        if self.camera_control_widget and self.camera_control_widget.isVisible():
            self.camera_control_widget.hide()
            return True
        else:
            return False

    def hide_ir_camera_set_widget(self):
        """IR 카메라 설정 위젯 숨김"""
        if self.ir_camera_set_widget and self.ir_camera_set_widget.isVisible():
            self.ir_camera_set_widget.hide()
            return True
        else:
            return False

    # --------------------------
    # 하단 위젯 표시 관련
    # --------------------------
    def show_bottom_widget(self, skip=False):
        """하단 위젯 표시/토글(초기 표시와 클릭 토글을 분리)"""

        # 레이아웃 및 시그널 연결은 1회만
        if not self._bottom_move_connected:
            self.bottom_widget.moveLocationRequested.connect(self.center_map_on_tracked)
            self._bottom_move_connected = True

        if self.bottom_widget.parent() is None:
            self.main_layout.addWidget(self.bottom_widget, 1, 0)

        if not skip:
            if not self.bottom_toggle_state:
                # ON: 표시
                if self.device_data:
                    self.bottom_widget.set_camera_pitch(self.device_data.get('camera_pitch'))
                self.bottom_widget.show()
                self.bottom_toggle_state = True
            else:
                # OFF: 숨김
                self.bottom_widget.hide()
                self.bottom_toggle_state = False
            return

        # 초기 1회: 하단만 강제 표시 (토글 상태에는 영향 주지 않음)
        if not self.bottom_widget_alert_shown:
            if getattr(self.bottom_widget, "radio_around_patrol", None) and self.bottom_widget.radio_around_patrol.isChecked():
                QMessageBox.information(
                    self,
                    "Round View",
                    "현재 카메라 Yaw,Pitch 각도를 기준으로 작동합니다.\n (yaw 값은 ± 30º 주기적으로 변경,Pitch 값은 고정)"
                )
            self.bottom_widget_alert_shown = True

        if self.device_data:
            self.bottom_widget.set_camera_pitch(self.device_data.get('camera_pitch'))

        self.bottom_widget.show()
        # bottom_toggle_state는 초기 표시를 '무시'하도록 False 유지
    
    def center_map_on_tracked(self):
        """현재 추적 위치로 지도 중심 이동"""

        js_code = """
        if (typeof focusTracked === 'function') { focusTracked(); }
        """
        self.web_view.page().runJavaScript(js_code)
        
    def update_cursor_latlng(self, lat, lng):
        if self.bottom_widget:
            self.bottom_widget.set_location(lat, lng)
    # --------------------------
    # 데이터 처리 관련
    # --------------------------


    def update_device_data(self):
        """지도 및 위젯 데이터 업데이트"""
        data = self.protocol.get_mission_device_log()
        if not data:
            # 추적 제거 및 카메라 위젯 플레이스홀더 표시
            js_code = """
            if (typeof clearTracked === 'function') { clearTracked(); }
            """
            self.web_view.page().runJavaScript(js_code)
            return
        data_date=data.get('date')
        data_date = datetime.fromisoformat(data_date)
        now = datetime.now(timezone(timedelta(hours=9)))
        three_minutes_ago = now - timedelta(minutes=3) #3분 이내 데이터 여부 파악용 
        if data_date >= three_minutes_ago:
            if self.camera_md_data_widget and self.camera_md_data_widget.isVisible():
                try:
                    self.camera_md_data_widget.update_data(data,isIR)
                except Exception as e:
                    print(f"⚠️ 다이얼로그 데이터 업데이트 오류: {e}")
            if hasattr(self.bottom_widget, "set_interactive_enabled"):
                self.bottom_widget.set_interactive_enabled(True)
            else:
                try:
                    self.bottom_widget.button_move_location.setEnabled(True)
                    self.bottom_widget.button_start_patrol.setEnabled(True)
                    self.bottom_widget.radio_around_patrol.setEnabled(True)
                except Exception as e:
                    print(f"⚠️ 하단 위젯 활성화 오류: {e}")
        else:
                if self.camera_md_data_widget:
                    try:
                        self.camera_md_data_widget.set_no_data() #3분 이내 데이터 없는 경우 -로 표기
                    except Exception as e:
                        print(f"⚠️ 카메라 데이터 '-' 표시 오류: {e}")

                # 하단 위젯 표시 + 비활성화
                if hasattr(self.bottom_widget, "set_interactive_enabled"):
                    self.bottom_widget.set_interactive_enabled(False)
                else:
                    try:
                        self.bottom_widget.button_move_location.setEnabled(False)
                        self.bottom_widget.button_start_patrol.setEnabled(False)
                        self.bottom_widget.radio_around_patrol.setEnabled(False)
                    except Exception as e:
                        print(f"⚠️ 하단 위젯 비활성화 오류: {e}")

        

        # 정상 연결 시 최초 1회 하단만 강제 표시
        self.show_bottom_widget(True)
        self.no_device_message_shown = False

        self.device_data = data
        js_code = f"""
        if (typeof updateDroneData === 'function') {{
            updateDroneData({json.dumps(data)},{json.dumps(camera_md_data_widget_module.TITLE_NAME )});
        }}
        """
        self.web_view.page().runJavaScript(js_code)

        # BottomWidget에 카메라 pitch 전달
        if self.bottom_widget:
            try:
                self.bottom_widget.set_camera_pitch(data.get('camera_pitch'))
            except Exception as e:
                print(f"⚠️ BottomWidget pitch 업데이트 오류: {e}")


    # --------------------------
    # 이벤트 핸들러
    # --------------------------
    def update_fire_sensor_circles(self):
        """센서 상태에 따라 지도 원 색상 업데이트"""
        statuses = []
        try:
            if self.fire_sensor_widget:
                statuses = self.fire_sensor_widget.get_sensor_statuses()
                _now_flags_index=[flag.get('flags') for flag in statuses]
                _now_gas_index=[gas.get('gas_index') for gas in statuses]

                if self.previous_gas_index and self.previous_flags_index:
                    # 변화가 발생한 센서 인덱스 수집
                    triggered_indices = [
                        i for i in range(len(_now_gas_index))
                        if (
                            self.previous_gas_index[i] != 100 and _now_gas_index[i] == 100 and _now_flags_index[i] == 1
                        ) or (
                            self.previous_flags_index[i] != 1 and _now_flags_index[i] == 1 and _now_gas_index[i] == 100
                        )
                    ]
                    # 센서별 개별 메시지 표시
                    for idx in triggered_indices:
                        message = f"{idx+1}번째 센서에서 산불이 감지되었습니다."
                        js_msg = f"""
                        if (typeof showTopMessage === 'function') {{
                            showTopMessage({json.dumps(message)}, {{ type: 'warn', size: 'large', centerSensorIndex: {idx} }});
                        }}
                        """
                        self.web_view.page().runJavaScript(js_msg)

                self.previous_flags_index=_now_flags_index
                self.previous_gas_index=_now_gas_index

        except Exception as e:
            print(f"⚠️ FireSensor 상태 생성 오류: {e}")

        js_code = f"""
        if (typeof setFireSensorColors === 'function') {{
            setFireSensorColors({json.dumps(statuses)});
        }}
        """
        self.web_view.page().runJavaScript(js_code)

    def on_load_finished(self, ok):
        if ok:
            print("✅ HTML 로딩 완료!")
            js_init_code = """
            new QWebChannel(qt.webChannelTransport, function(channel) {
                window.pyHandler = channel.objects.pyHandler;
                console.log("WebChannel 연결 완료");
            });
            """
            self.web_view.page().runJavaScript(js_init_code)
            self.update_device_data()
            # 초기 산불센서 색상 적용
            try:
                self.update_fire_sensor_circles()
            except Exception as e:
                print(f"⚠️ FireSensor 색상 적용 오류: {e}")
        else:
            print("❌ HTML 로딩 실패")

    # --------------------------
    # 등록지점 마커
    # --------------------------
    def set_marker_inputs(self, degree: float, zoom: int, lat: float = None, lng: float = None):
        """map.html에서 전달된 마커 각도/줌 값 및 선택 위치 저장"""
        try:
            self.point_degree = degree
            self.point_zoom = zoom
            if lat is not None and lng is not None:
                self.point_lat = lat
                self.point_lng = lng

        except Exception as e:
            print(f"❌ 마커 입력 저장 오류: {e}")

    def delete_all_markers(self):
        "모든 marker 제거"
        self.db_poi.site_id=protocol_module.SITE_ID
        self.db_poi.delete()
    
    def delete_marker(self,poi_id):
        """poi_id에 해당하는 마커 삭제"""
        try:
            # site_id 설정 후 삭제 수행
            self.db_poi.site_id = protocol_module.SITE_ID
            # 1) 대상 poi 삭제
            self.db_poi.delete(poi_id)
            # 2) 이후 id들 재정렬 (poi_id > 삭제_id 인 것들 -1)
            self.db_poi.delete_poi(poi_id)
            print(f"마커 삭제 완료: poi_id={poi_id}")

            # 3) 변경된 POI 목록 재조회 및 지도 리프레시 (POI 마커 전부 삭제 → 다시 렌더링)
            try:
                self.db_poi_list = self.db_poi.select()
                pois = []
                for p in (self.db_poi_list or []):
                    pois.append({
                        'poi_id': getattr(p, 'poi_id', None),
                        'lat': getattr(p, 'latitude', None),
                        'lng': getattr(p, 'longitude', None),
                        'altitude': getattr(p, 'altitude', None),
                        'zoom_level': getattr(p, 'zoom_level', None)
                    })
                js_clear = (
                    "try {"
                    "  Object.keys(poiMarkers || {}).forEach(id => {"
                    "    try { map.removeLayer(poiMarkers[id]); } catch(e){}"
                    "    delete poiMarkers[id];"
                    "    if (poiData) delete poiData[id];"
                    "  });"
                    "} catch(e) { console.warn('poi clear error', e); }"
                )
                self.web_view.page().runJavaScript(js_clear)
                js_render = f"if (typeof renderPoiMarkers === 'function') {{ renderPoiMarkers({json.dumps(pois)}); }}"
                self.web_view.page().runJavaScript(js_render)
            except Exception as e:
                print(f"⚠️ POI 리프레시 오류: {e}")
        except Exception as e:
            print(f"❌ 마커 삭제 오류: {e}")

    def insert_poi_db(self,latitude,longitude,degree,zoom,site_id):
  
        # 기본 필드 설정
        self.db_poi.date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db_poi.site_id=site_id
        self.db_poi.latitude=latitude
        self.db_poi.longitude=longitude
        self.db_poi.altitude=degree
        self.db_poi.zoom_level=zoom

        # poi_id 설정정
        next_id = None
        self.db_poi.site_id = site_id
        next_id = self.db_poi.get_next_poi_id()
        self.db_poi.poi_id = next_id

        self.db_poi.insert()

    def update_poi_db(self,latitude,longitude,degree,zoom,site_id,poi_id):
        # 기본 필드 설정
        self.db_poi.date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db_poi.poi_id=poi_id
        self.db_poi.site_id=site_id
        self.db_poi.latitude=latitude
        self.db_poi.longitude=longitude
        self.db_poi.altitude=degree
        self.db_poi.zoom_level=zoom

        self.db_poi.update()
    
    # --------------------------
    # 입력 다이얼로그
    # --------------------------
    def show_tagert_angle_message(self):
        """각도 입력 다이얼로그 (-180 ~ 180)"""
        try:
            default = int(self.point_degree) if self.point_degree is not None else 0
        except Exception:
            default = 0
        val, ok = QInputDialog.getInt(
            self,
            "대상 각도 입력",
            "각도 (-180 ~ 180):",
            default,
            -180,
            180,
            1
        )
        return val if ok else None

    def show_tagert_zoom_message(self):
        """줌 입력 다이얼로그 (0 ~ 10)"""
        try:
            default = int(self.point_zoom) if self.point_zoom is not None else 0
        except Exception:
            default = 0
        val, ok = QInputDialog.getInt(
            self,
            "대상 확대/축소 수준",
            "줌 (0 ~ 10):",
            default,
            0,
            10,
            1
        )
        return val if ok else None

    def handle_sse_event(self, data):
        """SSE 이벤트 수신 처리: connect 포함 시 BottomWidget에서 출력"""
        try:
            # data가 이미 dict일 수 있으므로 중복 파싱을 피하고,
            # 문자열인 경우에만 JSON 파싱을 시도합니다.
            if isinstance(data, str):
                try:
                    parsed = json.loads(data)
                    data = parsed
                except Exception:
                    # 유효한 JSON이 아니면 원본 문자열을 그대로 사용
                    pass

            # 안전하게 로깅 (dict일 때만 .get 사용)
            cmd_val = data.get('cmd') if isinstance(data, dict) else None
            # print(f"main App {data},{type(data)},{cmd_val}")

            if isinstance(data, dict):
                if self.bottom_widget:
                    self.bottom_widget.receive_connect_signal(data)
                if self.ir_camera_set_widget and isIR:
                    self.ir_camera_set_widget.set_radio_image_sensor(data)
            else:
                # dict가 아닌 이벤트(문자열/기타)는 현재 처리하지 않음
                # 필요 시 특정 문자열 이벤트에 대한 분기 추가 가능
                pass
        except Exception as e:
            print(f"❌ SSE 이벤트 처리 오류: {e}")
            import traceback
            traceback.print_exc()
        return

    # 사이트 선택 창 오류 처리
    # --------------------------
    def on_device_dialog_accepted(self):
        global isIR
        """OK 후 유효한 시리얼이 설정되었는지 확인하고 SSE 재시작"""
        self.device_selection_resolved = True

        if getattr(protocol_module, "DEVICE_NAME", ""):
            # 새 DEVICE_NAME으로 SSE 재접속
            self.setup_sse_event()

            # 클릭 토글 상태는 초기 표시를 '무시'하도록 False로 유지
            self.bottom_toggle_state = False

            camera_serial=self.protocol.get_camera_serial_number()
            
            if "IR" in camera_serial:
                isIR=True
            else:
                isIR=False
            if getattr(protocol_module,"SITE_ID",""):
                # site_id에 매핑된 poi 마커 가져오기기
                self.db_poi.site_id=protocol_module.SITE_ID
                self.db_poi_list=self.db_poi.select()
                # 지도에 POI 마커 렌더링 요청
                try:
                    pois = []
                    for p in (self.db_poi_list or []):
                        pois.append({
                            'poi_id': getattr(p, 'poi_id', None),
                            'lat': getattr(p, 'latitude', None),
                            'lng': getattr(p, 'longitude', None),
                            'altitude': getattr(p, 'altitude', None),
                            'zoom_level': getattr(p, 'zoom_level', None)
                        })
                    js = f"if (typeof renderPoiMarkers === 'function') {{ renderPoiMarkers({json.dumps(pois)}); }}"
                    self.web_view.page().runJavaScript(js)
                except Exception as e:
                    print(f"❌ POI 렌더링 전달 오류: {e}")
        else:
            self.show_no_device_connected_message()
        

    def on_device_dialog_rejected(self):
        """취소 클릭 시 알림 표시"""
        self.device_selection_resolved = True
        self.show_no_device_connected_message()

    def show_no_device_connected_message(self):
        """임무장비 연결 없음 안내 메시지 (한 번만 표시)"""
        if self.no_device_message_shown:
            return
        QMessageBox.information(self, "알림", "연결된 임무장비 값이 없습니다")
        self.no_device_message_shown = True

        if self.camera_md_data_widget and self.camera_md_data_widget.isVisible():
            try:
                self.camera_md_data_widget.update_data(data,isIR)
            except Exception as e:
                print(f"⚠️ 다이얼로그 데이터 업데이트 오류: {e}")
    
# ------------------------------
# 실행부
# ------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapApp()
    sys.exit(app.exec())


