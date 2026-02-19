"""__init__ method + simple methods."""

class BankAccount:  # Create a BankAccount class (template)
    def __init__(self, owner, balance=0):  # Constructor: runs when account is created
        self.owner = owner  # Store owner name inside the object
        self.balance = balance  # Store starting balance (default is 0)

    def deposit(self, amount):  # Instance method: adds money to THIS account
        self.balance += amount  # Increase balance by amount

if __name__ == "__main__":  # Runs only when file is executed directly
    acc = BankAccount("Ali", 100)  # Create an account for Ali with balance 100
    print("start balance =", acc.balance)  # Print current balance
    acc.deposit(50)  # Deposit 50 into the account
    print("after deposit =", acc.balance)  # Print new balance
