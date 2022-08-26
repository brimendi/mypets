from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
from flask_app.models import pets_model
from flask_app.models import reminders_model

# PETS CONSTRUCTOR AND ATTRIBUTES 
class Pets:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.dob = data['dob']
        self.weight = data['weight']
        self.on_meds = data['on_meds']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['user_id']
        self.image_filename = data['image_filename']
        self.breed = data['breed']

    # method for creating a new pet
    @classmethod
    def create(cls, data):
        query = "INSERT INTO pets (name, dob, weight, on_meds, user_id, image_filename, breed) VALUES(%(name)s, %(dob)s, %(weight)s, %(on_meds)s, %(user_id)s, %(image_filename)s, %(breed)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    # method for editing a pet account 
    @classmethod
    def edit_pet(cls,data):
            query = "UPDATE pets SET name = %(name)s, dob = %(dob)s, weight = %(weight)s, on_meds = %(on_meds)s WHERE id = %(id)s"
            return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pets JOIN users ON pets.user_id=users.id"
        results = connectToMySQL(DATABASE).query_db(query)
        all_pets = []
        if results: 
            for row in results:
                this_pet = cls(row)
                user_data = {
                    **row,
                    'id': row['user_id']
                }
                # this_user = user_model.Users(user_data)
                # this_pet.planner = this_user
                all_pets.append(this_pet)
        return all_pets

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM pets WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        row = results[0]
        this_pet = cls(row)
        return this_pet

    @classmethod
    def get_all_by_user_id(cls, data):
        query = "SELECT * FROM pets WHERE user_id = %(user_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        user_pets = []
        if results: 
            for row in results:
                this_pet = cls(row)
                user_pets.append(this_pet)
        return user_pets


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM pets WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(form_info):
        is_valid = True
        if len(form_info['name']) < 1:
            flash("name is required")
            is_valid = False
        if len(form_info['dob']) < 1:
            flash("date of birth is required")
            is_valid = False
        if len(form_info['weight']) < 1:
            flash("weight is required")
            is_valid = False
        if "on_meds" not in form_info:
            flash("currently on medication? is required")
            is_valid = False
        return is_valid