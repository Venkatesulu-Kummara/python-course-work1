'''fa = eval(input("Follows Account:"))
if fa:
    cf = eval(input("close Friend:"))
    if cf:
        print("story Visible")
    else:
        print("Not in close friends list")
else:
    print("Follow the account First")'''
'''
reg = eval(input("Registered:"))
if reg:
    fee = eval(input("Fee paid:"))
    if fee:
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")'''
'''
Link = eval(input("Enter the Link Active:"))
if Link:
    permission = eval(input("Enter the Permission Granted:"))
    if permission:
        print("File Opened Successfully")
    else:
        print("Permission Denied")
else:
    print("invalid link")'''

data = {
    'Prabhs':{'status':True,'python':99,'mysql':98,'flask':99},
    'Anushka':{'status':True,'python':90,'mysql':95,'flask':92},
    'Virat':{'status':True,'python':89,'mysql':90,'flask':90},
    'Rohit':{'status':False,'python':None,'mysql':None,'flask':None},   
    'Rahul':{'status':True,'python':35,'mysql':42,'flask':30},
    'mahesh':{'status':True,'python':30,'mysql':60,'flask':70},
}

name = input("Enter the name:")
if name in data:
    if data[name]['status']:
        sum = data[name]['python']+ data[name]['mysql']+ data[name]['flask']
        avg = sum/3
        print(f'Hello {name}!!!!!')
        print(f'Your average score is: {avg}')
        print(f'your average score is {avg}')
        if avg>=90:
            print("outstanding performance")
        elif avg>=80:
            print("very good")
        elif avg>=70:
            print("good,work hard")
        elif avg>=35:
            print("better luck next time")
        else:
            print("fail,bring your parents")
    else:
        print(f'{name}  did not attempt the exam,bring your parents')
else:
    print(f'{name} is not found')