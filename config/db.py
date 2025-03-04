from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    # Basic configuration
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'travel_recomendation'
    app.config['MYSQL_PORT'] = 3306    
    app.config['MYSQL_POOL_SIZE'] = 5  # Número de conexiones en el pool
    app.config['MYSQL_POOL_NAME'] = 'mypool'
    
    mysql.init_app(app)
    app.mysql = mysql  
    
    return mysql