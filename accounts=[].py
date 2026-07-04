accounts=[]
class bankaccount:
    def __init__(self, name, accountnu, balance):
      self.name=name
      self.accountnu=accountnu
      self.balance=balance
    def withdraw(self):
      amount=float(input("enter your amount") )
      if self.balance>=amount:
        self.balance-=amount
        print("withdrwa suucessfuly")
      else:
        print("insufficient balance")
    def deposit(self):
       amount=float(input("enter your amount"))
       self.balance+=amount
       print("deposit suucessfuly")
    def checkbalance(self):
       print("your balnce is :",self.balance)
    
def addnew_account():
  name=input("enter your name")
  accountnu=int(input("enter your acccountnu"))
  balance=int(input("enter your balance"))
  account=bankaccount(name,accountnu,balance)
  accounts.append(account)
  print("account created sucessfuly")
def search_account():
  name=input("enter your name")
  for account in accounts:
    if (account.name==name):
      print("congratulation account found ")
      break
    else:
      print("account not found ")
def veiw_accounts():
  for account in accounts:
    print("all acounts show here:", "name",account.name,"\naccount no",account.accountnu,"\nbalance",account.balance)
def delete_account():
  name=input("enter your name")
  for account in accounts:
    if account.name==name:
      accounts.remove(account)
      print("account remove sucessfully")
      break
    else:
      print("account not found")
while True:
  print("1 addnewaccount")
  print("2 with drwa")
  print ("3 deposit")
  print ("4 serach account")
  print("5 delte acount")
  print("6 veiw all acount")
  print("7 check balance")
  print("8 exit")
  choice=int(input("enter your choice:"))
  if(choice==1):
    addnew_account()
  elif ( choice==2):
      if (accounts==[]):
        print("first you have to make account")
      else:
        name=input("enter your name")
        for account in accounts:
          if (account.name==name):
            account.withdraw()
  elif (choice==3):
      name=input("enter your name ")
      for account in accounts :
          if (account.name==name):
            account.deposit()
  elif(choice==4):
    search_account()
  elif(choice==5):
    delete_account()
  elif(choice==6):
    veiw_accounts()
  elif(choice==7):
    name=input("enter your name")
    for account in accounts:
      if account.name==name:
        account.checkbalance()
  else:
    break              






