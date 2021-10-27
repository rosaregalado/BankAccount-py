class BankAccount:
  def __init__(self, full_name, account_number, balance=0):
    self.fullName = full_name
    self.accountNumber = account_number
    self.balance = balance


  def deposit(self, amount):
    self.balance += amount
    print(f"Amount deposited: ${amount} New balance: ${self.balance}")


  def withdraw(self, amount):
    self.balance -= amount
    if self.balance < 0:
      print("Insufficient funds.")
      self.balance -= 10
      print(f"An overdraft fee of $10 has been charged to your account.")
    else:
      print(f"Amount withdrawn: ${amount}. \nRemaining balance: ${self.balance}")


  def get_balance(self):
    print(f"Account balance: ${self.balance}")
    return self.balance

  
  def add_interest(self):
    self.balance += 0.00083 * self.balance


  def display_account_number(self):
    display_account_number = (len(self.accountNumber) - 4) * "*"
    list_nums = list(self.accountNumber) [-4:]
    for num in list_nums:
      display_account_number += num
    return display_account_number  


  def print_statement(self):
    print(self.fullName)
    print(f"Account No.: {self.display_account_number()}")
    print(self.get_balance())



mitchell_account = BankAccount("Mitchell", "03141592")

mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
mitchell_account.withdraw(150)
mitchell_account.print_statement()




















































































































































































































































































