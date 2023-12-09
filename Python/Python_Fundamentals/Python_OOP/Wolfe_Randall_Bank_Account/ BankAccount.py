class BankAccount:
    # don't forget to add some default values for these parameters! 
    def __init__(self, int_rate, balance):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        # increases the account balance by the given amount
        self.balance += amount
        print(f"Deposited: ${amount}")
        return self

    def withdraw(self, amount):
        # decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5 
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        # print to the console: eg. "Balance: $100" 
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            print(f"Interest added: ${self.balance * self.int_rate}")
        return self
    
user1 = BankAccount(0.01, 0)
user1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

user2 = BankAccount(0.05, 0)
user2.deposit(200).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()
