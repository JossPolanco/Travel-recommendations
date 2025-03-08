from flask import request, jsonify

def get_general_info():
    try:     
        # Debug to know the info brough
        print("Content of request.form:", request.form)
        
        # Save all the info brough into variables
        origin = request.form["origin"]
        place = request.form["place"]
        distance = request.form["distance"]
        budget = request.form["budget"]
        weather = request.form["weather"]
        season = request.form["season"]
        
        # Dictionary of the data
        recommendation = {
            'origin': origin,
            'place': place,
            'distance': distance,
            'budget': budget,
            'weather': weather,
            'season': season
        }
        # Debug
        print("Successful search.", recommendation)
        # Converts the dictionray in json
        jsonify(recommendation)
        # Returns the json
        return recommendation
    except KeyError as e:
        print(f"{e}")        