'''
def functionname(arg)
   #statements
   return(optional)
functionname(parameters)
'''
'''
def gst(price):
    print("Original price:",price)
    print("Final price:",price+price*0.18)

gst(2000)
gst(6000)
gst(3000)
gst(7000)
gst(500)
'''
'''
def table(n):
    print(f"{n}-Table")
    print('----------------------------------------')
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}") 
for i in range(1,21): 
    table(i)
    '''
'''
def table(n):  #argument
    print(f"{n}-Table")
    print('----------------------------------------')
    for i in range(1,11): #incrementing frm 1 to 10
        print(f"{n} * {i} = {n*i}") # 5*2=10
table(5) #calling the function and passing the vale
'''
'''
def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "leap year"
    else:
        return "not a leap year"
print(isleap(2012)) #we use print while we use return else not required while calling a function
print(isleap(2030))
print(isleap(2016))
'''
'''
def prime(n):
    for i in range(2,n):
        if n%i == 0 :
            return"Not a prime number"
    else:
        return"prime number"
print(prime(99))
print(prime(16))
print(prime(7))
print(prime(11))
'''
'''
#4 types of arguments
positional
keyword
default
variable length arguments
'''
'''#positional arguments
def display(name,email,pwd):
    print("name",name)
    print("email",email)
    print("pwd",pwd)
display('abc','abc@gmail.com','abc@123')
display('abc@gmail.com','abc','abc@123')
display('abc@123','abc','abc@gmail.com')
'''
'''
#keyword based on keys it allocates the values
def display(name,email,pwd):
    print("name",name)
    print("email",email)
    print("pwd",pwd)
display(name='abc',email='abc@gmail.com',pwd='abc@123')
display(email='abc@gmail.com',name='abc',pwd='abc@123')
display(pwd='abc@123',name='abc',email='abc@gmail.com')
'''
'''
# default arg always shld be at the end of arg
def display(name,email,pwd=None):
    print("name",name)
    print("email",email)
    print("pwd",pwd)
display('abc','abc@gmail.com')
display('abc','xyz@gmail.com','abc@123')
'''
'''
#variable 
def display(*names):  # * is used for tuple formate 
    print(names)
display('abc')
display('xyz','wof')
display('abc','xyz')
display('abc','xyz','efg')
'''
#passing key and values-pairs use ** (dict)
def display(**names):  # ** is used for dict formate 
    print(names)
display(n1='abc')
display(n1='xyz',n2='xyz')