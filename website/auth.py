from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Log In</p>"

@auth.route('/signup')
def signup():
    return "<p>Sign Up</p>"

@auth.route('/logout')
def logout():
    return "<p>Log Out</p>"