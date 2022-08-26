from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import Users
from flask_app.models.pets_model import Pets
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# MAIN PAGE ** if user didnt log out it'll still take you to dashboard logged in page **
@app.route('/login_and_registration')
def login_and_register_form():
    if "user_id" in session:
        return redirect('/mypets/home')
    return render_template("login_and_registration.html")

# HOMEPAGE ** once logged in redirected here, if user id logged out it will not take you to homepage. reirected to log in 
@app.route('/mypets/home')
def homepage():
    if not "user_id" in session:
        return redirect('/login_and_registration')
    user = Users.get_by_id({'id': session['user_id']})
    all_pets = Pets.get_all()
    return render_template("home.html", all_pets = all_pets, user = user)

# Once registered directed to homepage/ validating register info/ hashing password/ storing new users info in database and session
@app.route('/users/register', methods=['POST'])
def register():
    # print(request.form)
    if not Users.validate(request.form):
        return redirect('/login_and_registration')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hashed_pw
    }
    session['user_id'] = Users.create(data)
    return redirect('/mypets/home')

# Once logged out the session is deleted and redirected to log in page 
@app.route('/users/logout')
def logout():
    if "user_id" in session:
        del session['user_id']
    return redirect('/login_and_registration')

#Log in validations/ Fetching user info by email. Validating log in info is in db/ storing log in in session/ redirectng to dashboard
@app.route('/users/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_from_db = Users.get_by_email(data)
    if not user_from_db:
        flash("Invalid credentials", "log")
        return redirect('/login_and_registration')
    if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        flash("Invalid credentials", "log")
        return redirect('/login_and_registration')
    session['user_id'] = user_from_db.id
    return redirect('/mypets/home')