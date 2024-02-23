
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('Dojos_and_Ninjas_CRUD').query_db(query)
        dojos = results
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('CURD_User').query_db(query)
        users = results
        users = []
        for user in results:
            users.append(cls(user))
        return users



    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('Dojos_and_Ninjas_CRUD').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = """SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id 
        WHERE dojos.id = %(id)s;"""""
        
        results = connectToMySQL('Dojos_and_Ninjas_CRUD').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                "id": row['ninjas.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['ninjas.created_at'],
                "updated_at": row['ninjas.updated_at'],
                "dojo_id": row['dojo_id']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo