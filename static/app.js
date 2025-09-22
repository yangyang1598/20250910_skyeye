// === 지도 초기화 ===
const map = L.map("map", {
    center: [37.5665, 126.9780],
    zoom: 15
  });
  
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: "&copy; OpenStreetMap contributors"
  }).addTo(map);
  
  // === 이미지 아이콘 ===
  const imgIcon = L.icon({
    iconUrl: "https://upload.wikimedia.org/wikipedia/commons/7/7e/Boat_icon.png",
    iconSize: [60, 60],
    iconAnchor: [30, 30]
  });
  
  // 마커 전역 변수
  let imgMarker = null;
  
  // === 마커 업데이트 ===
  function updateMarker(lat, lng) {
    if (!imgMarker) {
      imgMarker = L.marker([lat, lng], { icon: imgIcon }).addTo(map);
    } else {
      imgMarker.setLatLng([lat, lng]);
    }
  }
  
  // === 주기적으로 GPS 요청 (2초마다) ===
  setInterval(() => {
    fetch("/gps")
      .then(res => res.json())
      .then(data => {
        updateMarker(data.lat, data.lng);
      })
      .catch(err => console.error("GPS 불러오기 실패:", err));
  }, 2000);
  