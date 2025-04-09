from flask import Blueprint, jsonify, request
from models.places_model import PlacesModel

bp = Blueprint('api', __name__)

# We create an object if the model to acces its methods
place_model = PlacesModel()

@bp.route("/place/limit/<int:limit>")
def places(limit):
    # Brings a limited number of places
    response = place_model.get_places_by_limit(limit)
    # returns the response data in json format
    return jsonify(response)


# URl with an id like parameter
@bp.route("/place/<place_id>")
def go_place(place_id):
    # We access to its method to bring all data o the place by id
    response = place_model.get_places_by_id(place_id)    
    # returns the response data in json format
    return jsonify(response)


@bp.route("/search", methods=["POST"])
def search():
    try:
        # Brings the json sended by the uri in json format
        data = request.get_json()        
        # Saves each value from the json 
        origin = data.get('origin')
        destiny = data.get('destiny')
        distance = data.get('distance')
        budget = data.get('budget')
        weather = data.get('weather')
        season = data.get('season')
        # Calls to the method to bring all the places than matches with the data
        response = place_model.get_places_by_info(destiny, distance, budget, weather, season)
        # returns the response data in json format
        return jsonify(response)
        
    except KeyError as e:
        print(f"{e}")        
        return jsonify(response)