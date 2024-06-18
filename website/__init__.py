from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CSC520 Group 6'

    #registering blueprints
    #------------------------
    #importing blueprints from other files
    from .views import views
    from .auth import auth

    #registering
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app