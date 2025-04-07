from flask import Blueprint, render_template, current_app, jsonify
from models.places_model import PlacesModel
from mapkick.flask import Map

bp = Blueprint("place", __name__)

