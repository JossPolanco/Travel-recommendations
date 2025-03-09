from flask import Blueprint, render_template
from models.places_model import PlacesModel

bp = Blueprint("place", __name__)

@bp.route("/place/<place_id>")
def go_place(place_id):
    
    place_model = PlacesModel()
    
    place = place_model.get_places_by_id(place_id)
    
    return render_template("place.html", place=place)