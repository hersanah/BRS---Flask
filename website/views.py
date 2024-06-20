from flask import Blueprint, render_template, Flask
from flask_login import current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html", user=current_user)


@views.route('/user-gender/<user>')
def select_gender(user):

    return render_template("gender-selection.html", data=user, first_name="Test")