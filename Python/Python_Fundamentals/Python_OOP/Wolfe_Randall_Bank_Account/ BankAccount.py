class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        
        
    def deposit(self, amount):
        # increases the account balance by the given amount
        amount += self.balance
        print(amount)
        return amount
        
    def withdraw(self, Withdraw_amount):
        # decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        Withdraw_amount =  Withdraw_amount - self.balance
        print(Withdraw_amount)
        if Withdraw_amount < 0:
            Withdraw_amount = Withdraw_amount - 5 
            print(Withdraw_amount)
            print("Insufficient funds: Charging a $5 fee: " + str(Withdraw_amount))
        return Withdraw_amount
        
    def display_account_info(self):
        # print to the console: eg. "Balance: $100"
        print(self.balance)
        
    def yield_interest(self):
        # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        self.balance = self.balance * self.int_rate
        
account1 = BankAccount(0.01, 100)
account1.deposit(0)
account1.withdraw(60)
