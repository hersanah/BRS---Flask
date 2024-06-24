import json

from flask import Blueprint, render_template, Flask, request, redirect, url_for
from flask_login import current_user
from . import mysql

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html", user=current_user)


@views.route('/user-gender/<user>', methods=['POST', 'GET'])
def select_gender(user):

    if request.method == 'POST':
        
        button=request.form.to_dict()
        gender = ''
                
        for values in button:            
            gender=values
        
        cur = mysql.connection.cursor()
        cur.execute('''
            UPDATE users
            set gender=%s
            where id=%s
        ''', (gender, user))
        
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('views.select_genre', user=user))
    
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT first_name
        FROM users
        WHERE id = %s
    ''', [user])
    returnedname = cur.fetchone()
    cur.close()

    name = returnedname[0].lower().capitalize()

    return render_template("gender-selection.html", first_name=name)


@views.route('/genre-selection/<user>', methods=['POST', 'GET'])
def select_genre(user):
    if request.method == 'POST':

        selected_genres = request.form.get('selectedGenres')

        # Parse the JSON string to a Python list (if needed)
        genres_list = json.loads(selected_genres)

        # Convert the list to a JSON string for storage
        genres_json = json.dumps(genres_list)

        cur = mysql.connection.cursor()
        cur.execute('''
            UPDATE users
            SET fav_genre=%s
            WHERE id=%s
        ''', (genres_json, user))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('views.path_to_reading', user=user))

    return render_template("genre-selection-2.html", user=user)


@views.route('/enjoy/<user>', methods=['POST', 'GET'])
def path_to_reading(user):
    return render_template("reading.html", user=user)

@views.route('/books/<user>', methods=['POST', 'GET'])
def recommend_books(user):
    return render_template("book-recommendations.html", user=user)

