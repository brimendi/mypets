from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import Users
from flask_app.models.pets_model import Pets
from flask_app.models.reminders_model import Reminders
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/mypets/reminders')
def reminders():
    if not "user_id" in session:
        return redirect('/')
    user = Users.get_by_id({'id': session['user_id']})
    all_reminders = Reminders.get_all()
    return render_template("reminders.html", all_reminders = all_reminders, user = user)

@app.route('/mypets/reminders/add')
def add_reminder():
    if not "user_id" in session:
        return redirect('/')
    user = Users.get_by_id({'id': session['user_id']})
    data = {
        'id': id
    }
    reminder = Reminders.create_reminder(data)
    return render_template("add_reminder.html", user = user, reminder = reminder)

@app.route('/mypets/reminders/create', methods=['POST'])
def create_reminder():
    if not "user_id" in session:
        return redirect('/')
    if not Reminders.validator(request.form):
        return redirect('/mypets/reminders/add')
    data = {
        **request.form, 
        'users_id': session['user_id']
    }
    Reminders.create_reminder(data)    
    return redirect('/mypets/reminders')