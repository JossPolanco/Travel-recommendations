from utils.db_utils import get_cursor

class PlacesModel:
    # Constructor
    def __init__(self):
        self.cur = None
    # Method to get the cursor
    def openCursor(self):
        if not self.cur:
            self.cur = get_cursor()
    # Method to close the cursor
    def closeCursor(self):
        if self.cur:
            self.cur.close()
            self.cur = None
    # Method that brings all places 
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
    # Method to get all the places limited by a number
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
    # Method to get all the places that matches with the specifications provided by the user
    def get_places_by_info(self, place, distance, budget, weather, season):
        try:
            self.openCursor()
            # Query that calls a storaged procedure in the db and values to insert it like input in the storaged procedure
            query = "CALL prd_get_places(%s, %s, %s, %s, %s)"
            values = (place, distance, budget, weather, season)            
            self.cur.execute(query, values)
            result = self.cur.fetchall()                                    
            # Convert the result to a list of dictionaries
            columns = [col[0] for col in self.cur.description] #.description bring info of each column, col[0] bring the name of each column and we create a list
            result = [dict(zip(columns, row)) for row in result] #We iterate in each row, then we combine each row with columns creating key-value and converting it into a dict
            # Returns all the data from the database
            return result
        except KeyError as e:
            print(f"Error: {e}")
        finally:
            self.closeCursor()