class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        
    def deposit(self, amount):
        # deposit(self, amount) - increases the account balance by the given amount
        
    def withdraw(self, amount):
        # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        
    def display_account_info(self):
        # display_account_info(self) - print to the console: eg. "Balance: $100"
        
    def yield_interest(self):
        # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
