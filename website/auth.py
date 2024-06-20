from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import mysql

auth = Blueprint('auth', __name__)

@auth.route('/login/<existence>', methods=['GET', 'POST'])
def login(existence):

    if existence == 1:
        flash('Account already exists', category='error')

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        cursor = mysql.connection.cursor()
        cursor.execute('''
            SELECT * from users
            WHERE email = email
        ''')
        user = cursor.fetchall()
        cursor.close()

        return render_template("home.html", data=user)
    return render_template("signin.html", existence=0)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        # Get form data
        userDetails = request.form
        
        email = userDetails['email']
        first_name = userDetails['firstName']
        last_name = userDetails['lastName']
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
            #  reidrect existing user to log in page
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
                (email, first_name, last_name, password)
            )
            mysql.connection.commit()
            cur2.execute('''
            select id from users
            where email= %s
            ''', [email])
            userid = cur2.fetchone()
            cur2.close()
            flash('Account Created!', category='success')
            print(userid[0])
            return redirect(url_for('views.select_gender', user=userid))

    return render_template("signup.html")

# @auth.route('/logout')
# def logout():
#     return "<p>Log Out</p>"