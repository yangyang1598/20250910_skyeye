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
            print(f"site_id: {self.site_id}")
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

    def delete(self):
        db = DATABASE()
        params = []
        
        try:
            print(f"site_id: {self.site_id}")
            sql = f"""DELETE FROM {self.TABLE_NAME} WHERE site_id = %s"""
            params.append(self.site_id)

            rows = db.execute(sql, params)
            return rows
        except Exception as e:
            print(f"delete error: {e}")
            return None