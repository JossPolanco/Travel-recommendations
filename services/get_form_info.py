from flask import request
from models.places_model import PlacesModel

def get_general_info():
    try:
        # Debug to know the info brought
        print("Content of request.form:", request.form)
        
        # Save all the info brought from the form into variables
        origin = request.form["origin"]
        place = request.form["place"]
        distance = request.form["distance"]
        budget = request.form["budget"]
        weather = request.form["weather"]
        season = request.form["season"]
        
        # Dictionary of the data
        specifications = {
            'origin': origin,
            'place': place,
            'distance': distance,
            'budget': budget,
            'weather': weather,
            'season': season
        }
        # Debug
        print("Successful search.", specifications)
        
        # We create an object if the model to acces its methods
        places_model = PlacesModel()
        # We pass each value provided by the user to the method to select all the places that matches with the values in the db
        recommendations = places_model.get_places_by_info(specifications["place"], specifications["distance"], specifications["budget"], specifications["weather"], specifications["season"])
        # Returns all the places
        return recommendations
    except KeyError as e:
        print(f"{e}")
        return []