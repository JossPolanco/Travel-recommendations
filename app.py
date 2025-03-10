from flask import Flask
from config.db import init_db
from routes import index, search, place
from mapkick.flask import mapkick_blueprint

app = Flask(__name__)
mysql = init_db(app)

app.register_blueprint(index.bp)
app.register_blueprint(search.bp)
app.register_blueprint(place.bp)
app.register_blueprint(mapkick_blueprint)


if __name__ == "__main__":
    app.run(port=9000, debug=True)