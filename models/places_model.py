from utils.db_utils import get_cursor

class PlacesModel:
    def __init__(self):
        self.cur = None
        
    def openCursor(self):
        if not self.cur:
            self.cur = get_cursor()
    
    def closeCursor(self):
        if self.cur:
            self.cur.close()
            self.cur = None
    def get_places(self):
        try:
            self.openCursor()
            query = "SELECT * FROM places"
            self.cur.execute(query)
            return self.cur.fetchall()
        except KeyError as e:
            print(f"Error: {e}.")
        finally:
            self.closeCursor()
    def get_places_limited(self, limit):
        try:
            self.openCursor()
            query = "SELECT * FROM places LIMIT %s"
            self.cur.execute(query, (limit,))
            return self.cur.fetchall()
        except KeyError as e:
            print(f"Error: {e}.")
        finally:
            self.closeCursor()
    def get_places_by_info(self, place, distance, budget, weather, season):
        self.openCursor()
        
        query = "SELECT * FROM places WHERE place LIKE %s AND distance "