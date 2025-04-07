from flask import Blueprint, render_template

bp = Blueprint("index", __name__)

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/place/detailed/<int:id>')
def gallery(id):
    endpoint = ""