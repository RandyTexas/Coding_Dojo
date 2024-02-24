
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self, data):
        print("from class",data)
        self.id = data['id']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo;"
        results = connectToMySQL('Dojos_and_Ninjas_CRUD').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos




    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojo (location) VALUES (%(location)s);"
        return connectToMySQL('Dojos_and_Ninjas_CRUD').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = """SELECT * FROM dojo LEFT JOIN ninja ON dojo.id = ninja.dojo_id 
        WHERE dojo.id = %(id)s;""" 
        
        results = connectToMySQL('Dojos_and_Ninjas_CRUD').query_db(query, data)
        dojo = cls(results[0])
        
        for row in results:
            ninja_data = {
                "id": row['ninja.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['ninja.created_at'],
                "updated_at": row['ninja.updated_at'],
                "dojo_id": row['dojo_id']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo