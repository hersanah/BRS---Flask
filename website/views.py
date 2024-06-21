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

        return render_template("genre-selection.html")
    
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