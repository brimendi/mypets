from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
from flask_app.models import pets_model
from flask_app.models import budget_model

class Reminders:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.date = data['date']
        self.time = data['time']
        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM reminders JOIN users ON reminders.users_id=users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_reminders = []
        if results: 
            for row in results:
                this_reminder = cls(row)
                user_data = {
                    **row,
                    'id': row['users_id']
                }
                this_user = user_model.Users(user_data)
                this_reminder.planner = this_user
                all_reminders.append(this_reminder)
        return all_reminders

    @classmethod
    def create_reminder(cls, data):
        query = "INSERT INTO reminders (name, date, time, address, users_id) VALUES(%(name)s, %(date)s, %(time)s, %(address)s, %(users_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def edit_reminder(cls,data):
            query = "UPDATE reminders SET name = %(name)s, date = %(date)s, time = %(time)s, address = %(address)s WHERE id = %(id)s"
            return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validator(form_info):
        is_valid = True
        if len(form_info['name']) < 1:
            flash("name is required")
            is_valid = False
        if len(form_info['date']) < 1:
            flash("date is required")
            is_valid = False
        return is_valid