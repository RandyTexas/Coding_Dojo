from flask_app.config.mysqlconnection import connectToMySQL





class Users:
    db = 'Users'  
    
    def __init__(self,data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.id = data['id']
        self.created_at = data['created_at']    
        self.updated_at = data['updated_at']    
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('Users').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def save_users(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        print(query)
        return connectToMySQL('Users').query_db(query,data)
    
    