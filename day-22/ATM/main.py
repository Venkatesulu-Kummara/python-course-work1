data ={
    123456:{'name':"prabha",'pin':1234,'balance':100000,'history':[]},
    234561:{'name':"lucky",'pin':1234,'balance':200000,'history':[]},
    345612:{'name':"jaya",'pin':1234,'balance':300000,'history':[]},
}
def login():
    global acc_num
    acc_num = int(input("Enter your account number: "))
    pin = int(input("Enter the pin:"))
    if acc_num in data and data[acc_num]['pin']==pin:
      print("login successful")
      return True
    else:
       print("Invalid login ")

def menu():
   print(f"welcome to ATM {data[acc_num]['name']}")
   print("[C]heck Balance")
   print("[D]eposit")
   print("[W]ithdraw")
   print("[T]ransaction")
   print("[E]xit")

def check_balance():
   print(f'hello {data[acc_num]["name"]}')
   print(f"Your balace is:{data[acc_num]['balance']}")

def deposit():
    amount = int(input("Enter the amount to deposit: "))
    data[acc_num]['balance'] += amount
    data[acc_num]['history'].append(f"{amount} is deposited")
    print(f"{amount} Successfully deposited ")
    check_balance()

def withdraw():
    amount = int(input("Enter the amount to withdraw: "))
    if data[acc_num]['balance']>=amount:
        data[acc_num]['balance'] -= amount
        data[acc_num]['history'].append(f"{amount} is withdrawn")
        print(f"{amount} Successfully withdrawn")
    else:
        print("Insufficient balance.")
        check_balance()

def transaction():
    if data[acc_num]['history']:
        print("----------------Transaction History---------------")
        for i in data[acc_num]['history']:
           print(i)
        else:
            print("-------------End of History")
    else:
        print("No transaction history available.")