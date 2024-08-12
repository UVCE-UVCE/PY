class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Not enough balance.")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} successfully deposited.")

    def check_balance(self):
        print(f"The balance is {self.balance}")

# Initial balance setup
initial_balance = float(input("Enter the opening balance: "))
account = BankAccount(initial_balance)

loop_runner = True

while loop_runner:
    print("\nBank Account Operations")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

    option = int(input("Choice: "))

    if option == 1:
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif option == 2:
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif option == 3:
        account.check_balance()
    elif option == 4:
        loop_runner = False
        print("Exiting the program.")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
