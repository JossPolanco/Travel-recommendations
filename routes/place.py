from flask import Blueprint, render_template, current_app
from models.places_model import PlacesModel
from mapkick.flask import Map

bp = Blueprint("place", __name__)

# URl with an id like parameter
@bp.route("/place/<place_id>")
def go_place(place_id):
    # We create an object if the model to acces its methods
    place_model = PlacesModel()
    # We access to its method to bring all data o the place by id
    place = place_model.get_places_by_id(place_id)    
    
    mapkick_api_key = current_app.config['MAPKICK_API_KEY']
    map = Map([{'latitude': place['latitude'], 'longitude': place['longitude']}], api_key=mapkick_api_key)
    # We render the page and pass it all data
    return render_template("place.html", place=place, map=map, mapkick_api_key=mapkick_api_key)