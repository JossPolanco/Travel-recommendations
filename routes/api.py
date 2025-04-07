from flask import Blueprint, jsonify
from models.places_model import PlacesModel
from mapkick.flask import Map
from services.get_form_info import get_general_info

bp = Blueprint('api', __name__)

# We create an object if the model to acces its methods
place_model = PlacesModel()

@bp.route("/place/limit/<int:limit>")
def places(limit):
    # Brings a limited number of places
    response = place_model.get_places_by_limit(limit)
    # returns the response data
    return jsonify(response)


# URl with an id like parameter
@bp.route("/place/<place_id>")
def go_place(place_id):
    
    # We access to its method to bring all data o the place by id
    place = place_model.get_places_by_id(place_id)    
    
    map = Map([{'latitude': place['latitude'], 'longitude': place['longitude']}], zoom=4)
    # We render the page and pass it all data
    # return render_template("place.html", place=place, map=map, mapbox_token=current_app.config["MAPBOX_ACCESS_TOKEN"])
    return jsonify(place)


@bp.route("/search", methods=["POST"])
def search():
    try:
        # Brings the json sended by the uri
        info = get_general_info()  
        # Ensures that the info is collected correctly
        print("Printing info: ", info)   
        # We render the gallery and pass all the information collected   
        # return render_template("gallery.html", info=info)
        return jsonify(info)
    except KeyError as e:
        print(f"{e}")        
        # return render_template("gallery.html", info=[])
        return jsonify(info)