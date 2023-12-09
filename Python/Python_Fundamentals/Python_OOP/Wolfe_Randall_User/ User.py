class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

# Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, self.is_rewards_member, self.gold_card_points)
    
    # Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
    
    # have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        amount = self.gold_card_points
        x = x - amount
        print(amount)
        total = amount - x
        print(total)
        return total

user = User("Randall", "Wolfe", "randywolfe12@gmail.com", 25)

user.display_info()

user.enroll()
user.display_info()
user.spend_points()
user.display_info()
print(user.gold_card_points)

