data = {
    'oil' :200,
    'rice':1500,
    'flour':100,
    'sugar':80,
    'chillis':50,
    'wheat':100,
    'eggs':100,
    'peanuts':200,
    'butter':250,
    'bread':100,
}

for i in data:
    print(i.ljust(20),data[i])
bill = 0
while True:
    product = input("Enter the product name or [E]xit:")
    if product == 'E' or product =='e':
        print("thanks for shopping")
        print("Total bill:",bill)
        break
    else:
        quantity = int(input("Enter the quantity:"))
        bill += data[product]*quantity