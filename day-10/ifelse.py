'''username = input("username:")
password = input("password:")
if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Login failed")'''
'''
products = ["laptop", "mobile", "tablet"]
search = input("Enter the product to search: ")
if search in products:
    print(f"{search} is available")
else:
    print(f"{search} is not available")'''

price = int(input("Enter the price: "))
if price > 99:
    print("no delivery charges",price)
else:
    print("delivery charges apply",price+30)