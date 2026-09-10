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
prods = input("Enter the products:").split()
print("---------------bill--------------------")
bill = 0
for i in prods:
    print(i.ljust(20),data[i])
    bill += data[i]
print("Total bill".ljust(20),bill)