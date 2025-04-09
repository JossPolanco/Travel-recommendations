from flask import Blueprint, render_template, current_app
from mapkick.flask import Map
import requests

bp = Blueprint("index", __name__)

# default endpoint
@bp.route('/')
def index():
    return render_template("index.html")

# endpoint to call an specific place with the id
@bp.route('/place/detailed/<int:id>')
def gallery(id):
    # endpoint to call to the api
    endpoint = f"http://127.0.0.1:9000/place/{id}"
    # saves the response from the api
    response = requests.get(endpoint)
    # in case something happens it will give us the status code
    response.raise_for_status()
    # converts the response in json format
    place = response.json()
    # Creates the map and we give it the lat, lon and a zoom
    map = Map([{'latitude': place[10], 'longitude': place[11]}], zoom=4)
    # We render the page and pass it all data
    return render_template("place.html", place=place, map =map, mapbox_token=current_app.config["MAPBOX_ACCESS_TOKEN"])