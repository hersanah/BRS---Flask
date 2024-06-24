from flask import Flask
from flask_mysqldb import MySQL
import yaml

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    mysql.init_app(app)

    db = yaml.safe_load(open("website/db.yaml"))

    app.config['SECRET_KEY'] = 'CSC520 Group 6'
    app.config['MYSQL_HOST'] = db['mysql_host']
    app.config['MYSQL_USER'] = db['mysql_user']
    # app.config['MYSQL_PASSWORD'] = db['mysql_password']
    app.config['MYSQL_DB'] = db['mysql_db']

    #registering blueprints
    #------------------------
    #importing blueprints from other files
    from .views import views
    from .auth import auth

    #registering 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app