from flask import Flask
from config.db import init_db
from routes import index, search

app = Flask(__name__)
mysql = init_db(app)

app.register_blueprint(index.bp)
app.register_blueprint(search.bp)

if __name__ == "__main__":
    app.run(port=9000, debug=True)