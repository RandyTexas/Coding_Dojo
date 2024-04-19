from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_user(cls, data):
        print("hello", data)
        query = """INSERT INTO users (first_name, last_name, email, password) VALUES 
        (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        return connectToMySQL("login_flask").query_db(query, data)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("login_flask").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_user_login(data):
        is_valid = True
        if "email" not in data:
            flash("Invalid email address!")
            is_valid = False
        else:
            if len(data["email"]) < 2:
                flash("Welcome!")
                is_valid = False
            
        if len(data["email"]) < 2:
            is_valid = False
            
        if len(data["password"]) < 3:
            is_valid = False
            flash("Invalid password!")
            
        if not data["password"] :
            is_valid = False
        return is_valid
    
# create a regular expression object that we'll use later   
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# @staticmethod
# def validate_user(user):
#     is_valid = True
#     # test whether a field matches the pattern
#     if not EMAIL_REGEX.match(user['email']): 
#     flash("Invalid email address!")
#     is_valid = False
#     return is_valid