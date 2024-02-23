from flask_app.config.mysqlconnection import connectToMySQL


class Users:
    db = 'CURD_Users'  
    
    def __init__(self,data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.id = data['id']
        self.created_at = data['created_at']    
        self.updated_at = data['updated_at']    
        
        
    # Create
    @classmethod
    def save_users(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        print(query)
        return connectToMySQL('CURD_User').query_db(query,data)
    

    # Read
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
    def get_one(cls, user_id):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id': user_id}
        results = connectToMySQL('CURD_User').query_db(query, data)
        return cls(results[0])
    





    # Update
    # @classmethod   
    # def update(cls,data):
    #     query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
    #     results = connectToMySQL('CURD_User').query_db(query,data)
    #     return results

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('CURD_User').query_db(query,data)



    
    # Delete 
    # @classmethod
    # def delete(cls,data):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL('CURD_User').query_db(query,data)



    # the delete method will be used when we need to delete a friend from our database
    @classmethod
    def delete(cls, user_id):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": user_id}
        return connectToMySQL('CURD_User').query_db(query, data)
