from flask import Blueprint, render_template, jsonify
from services.get_form_info import get_general_info

bp = Blueprint('search', __name__)

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