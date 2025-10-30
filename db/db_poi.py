import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from db.database_test import DATABASE
class Poi:
    TABLE_NAME = 'poi'

    def __init__(self) -> None:
        self.date = ''
        self.poi_id = None
        self.site_id= None
        self.latitude = None
        self.longitude = None
        self.altitude = None
        self.zoom_level= None

    
    def select(self):
        db = DATABASE()
        params = []
        
        try:
            sql = f"""SELECT * FROM {self.TABLE_NAME} WHERE site_id = %s"""
            params.append(self.site_id)

            rows = db.fetch_all(sql, params)
            poi_list = []

            if rows:
                for r in rows:
                    poi = Poi()
                    poi.poi_id = r.get('poi_id')
                    poi.site_id = r.get('site_id')
                    poi.latitude = r.get('latitude')
                    poi.longitude = r.get('longitude')
                    poi.altitude = r.get('altitude')
                    poi.zoom_level = r.get('zoom_level')
                    poi_list.append(poi)

            return poi_list
        except Exception as e:
            print(f"select error: {e}")
            return None

    def get_next_poi_id(self):
        """현재 site_id 기준 최대 poi_id + 1 반환"""
        db = DATABASE()
        try:
            sql = f"""SELECT COALESCE(MAX(poi_id), 0) AS max_id FROM {self.TABLE_NAME} WHERE site_id = %s"""
            rows = db.fetch_all(sql, [self.site_id])
            max_id = 0
            if rows:
                r0 = rows[0]
                max_id = int(r0.get('max_id') or 0)
            return max_id + 1
        except Exception as e:
            print(f"get_next_poi_id error: {e}")
            return 1
            
    def delete(self):
        db = DATABASE()
        params = []
        
        try:

            sql = f"""DELETE FROM {self.TABLE_NAME} WHERE site_id = %s"""
            params.append(self.site_id)

            rows = db.execute(sql, params)
            return rows
        except Exception as e:
            print(f"delete error: {e}")
            return None

    def insert(self):
        db=DATABASE()
        params=[]
        try:
            print(f"insert: {self.date}, {self.poi_id}, {self.site_id}, {self.latitude}, {self.longitude}, {self.altitude}, {self.zoom_level}")
            sql=f"""INSERT INTO {self.TABLE_NAME} (date, poi_id, site_id, latitude, longitude, altitude, zoom_level) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            params.append(self.date)
            params.append(self.poi_id)
            params.append(self.site_id)
            params.append(self.latitude)
            params.append(self.longitude)
            params.append(self.altitude)
            params.append(self.zoom_level)
            return db.execute(sql, params)
        except Exception as e:
            print(f"insert error: {e}")
            return None
    
    def update(self):
        db=DATABASE()
        params=[]
        try:
            print(f"update: {self.date}, {self.poi_id}, {self.site_id}, {self.latitude}, {self.longitude}, {self.altitude}, {self.zoom_level}")
            sql=f"""UPDATE {self.TABLE_NAME} SET date=%s, latitude=%s, longitude=%s, altitude=%s, zoom_level=%s WHERE poi_id=%s AND site_id=%s"""
            params.append(self.date)
            params.append(self.latitude)
            params.append(self.longitude)
            params.append(self.altitude)
            params.append(self.zoom_level)
            params.append(self.poi_id)
            params.append(self.site_id)
            return db.execute(sql, params)
        except Exception as e:
            print(f"update error: {e}")
            return None