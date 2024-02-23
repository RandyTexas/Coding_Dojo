from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        self.dojo = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('Dojos_and_Ninjas_CRUD').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) 
        VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"""""
        
        return connectToMySQL('Dojos_and_Ninjas_CRUD').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        from flask_app.models.dojo import Dojo
        
        query = """SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.dojo_id = dojos.id 
        WHERE ninjas.id = %(id)s;"""""
        
        results = connectToMySQL('Dojos_and_Ninjas_CRUD').query_db(query, data)
        ninja = cls(results[0])
        dojo_data = {
            "id": results[0]['dojos.id'],
            "location": results[0]['location'],
            "created_at": results[0]['dojos.created_at'],
            "updated_at": results[0]['dojos.updated_at']
        }
        ninja.dojo = Dojo(dojo_data)
        return ninja