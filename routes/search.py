from flask import Blueprint, render_template, redirect
from services.get_form_info import get_general_info
bp = Blueprint('search', __name__)

@bp.route("/search", methods=["POST"])
def search():
    try:
        # Brings the json sended by the uri
        info = get_general_info()  
        print("imprimiendo la info: ", info)      
        return render_template("gallery.html", info=info)
    except KeyError as e:
        print(f"{e}")
    