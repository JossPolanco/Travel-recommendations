from flask import Blueprint, render_template, jsonify
from services.get_form_info import get_general_info

bp = Blueprint('search', __name__)

