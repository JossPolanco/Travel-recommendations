from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    # Basic configuration
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'travel_recommendations'
    app.config['MYSQL_PORT'] = 3306  
    
    mysql.init_app(app)
    app.mysql = mysql  
    
    return mysql