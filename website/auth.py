from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    return render_template("signin.html")

@auth.route('/signup', methods=['GET', 'POST'])
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
            #add user to database
            flash('Account Created!', category='success')


    return render_template("signup.html")

@auth.route('/logout')
def logout():
    return "<p>Log Out</p>"