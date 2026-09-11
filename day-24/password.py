import random

name = input("Enter your name:").title()
dob = input("enter you DOB[DD-MM-YYYY]:")

spc = ['@','#','%','&','*','.',',','$','&','/']
password = name[:3] + random.choice(spc) + dob[-4:] 
print("the generated pass is",password)