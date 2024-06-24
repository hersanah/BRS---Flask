from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import mysql

auth = Blueprint('auth', __name__)

@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        userDetails = request.form
        email = userDetails.get('email').lower()

        password = userDetails.get('password')

        cursor = mysql.connection.cursor()

        cursor.execute('''
            SELECT * FROM users
            WHERE email = %s
        ''', [email])
        userData = cursor.fetchone()

        cursor.close()

        if userData is None:
            return redirect(url_for('auth.signup'))

        if check_password_hash(userData[4], password):
            if userData[5] is None:
                return redirect(url_for('views.select_gender', user=userData[0]))

            elif userData[6] is None:
                return redirect(url_for('views.select_genre', user=userData[0]))
            return render_template("book-recommendations.html")

    return render_template("signin-2.html")


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        # Get form data
        userDetails = request.form
        
        email = userDetails['email'].lower()
        first_name = userDetails['firstName'].lower()
        last_name = userDetails['lastName'].lower()
        password1 = userDetails['password1']
        password2 = userDetails['password2']

        # Checking if user exists
        cur1 = mysql.connection.cursor()
        cur1.execute('''
            select id from users
            where email= %s
        ''', [email])
        user = cur1.fetchone()
        cur1.close()

        if user:
            #  redirect existing user to log in page
            return redirect(url_for('auth.login', existence=1))
            
        # Checking form data
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
            password = generate_password_hash(password1, method='scrypt')

            #add user to database
            cur2 = mysql.connection.cursor()
            cur2.execute(
                '''INSERT INTO users(email, first_name, last_name, password)
                VALUES (%s, %s, %s, %s)''',
                (email, first_name.lower(), last_name.lower(), password)
            )

            mysql.connection.commit()

            cur2.execute('''
            select id from users
            where email= %s
            ''', [email])
            userid = cur2.fetchone()
            cur2.close()
            flash('Account Created!', category='success')

            return redirect(url_for('views.select_gender', user=userid[0]))

    return render_template("signup.html")
