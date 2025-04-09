from flask import Flask
from config.db import init_db
from routes import views, api
from mapkick.flask import mapkick_blueprint
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
mysql = init_db(app)

app.config['MAPBOX_ACCESS_TOKEN'] = os.getenv('MAPBOX_ACCESS_TOKEN')

app.register_blueprint(mapkick_blueprint)
app.register_blueprint(views.bp)
app.register_blueprint(api.bp)


if __name__ == "__main__":
    app.run(port=9000, debug=True)