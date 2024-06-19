from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import views, sqlApp

mysql = sqlApp()
authBlueprint = Blueprint('auth', __name__)

@authBlueprint.route('/login')
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    return render_template("signin.html")

@authBlueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be longer than 4 characters', category='error')

        elif len(first_name) < 2:
            flash('Invalid First Name', category='error')

        elif len(last_name) < 2:
            flash('Invalid Last Name', category='error')

        elif len(password1) < 8:
            flash('Password is too short', category='error')

        elif password1 != password2:
            flash('Password don\'t match', category='error')

        else:
            password = generate_password_hash(password1, method='sha256')
            #add user to database
            cursor = mysql.connection.cursor
            cursor.execute(
                '''INSERT INTO users VALUES (%s, %s, %s, %s)''', (email, first_name, last_name, password)
            )
            mysql.connection.commit()
            cursor.close()
            flash('Account Created!', category='success')
            return redirect(url_for(views.home))         

    return render_template("signup.html")

@authBlueprint.route('/logout')
def logout():
    return "<p>Log Out</p>"