from flask import Blueprint, render_template
from flask_login import current_user

viewsBlueprint = Blueprint('views', __name__)

@viewsBlueprint.route('/')
def home():
    return render_template("index.html", user=current_user)