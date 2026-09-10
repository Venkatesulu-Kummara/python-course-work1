#varible declared inside function and can be acccessed inside 
# the function not outside the function=> LOCAL VARIABLE 
#varible declared outside function 
# it can be accesed any whr in prgm  => GLOBAL VARIABLE 
'''
def display():

    print("inside the function:",n)
n=10 #global declaration
display()
print("outside the function:",n)
'''
'''
def display():
    n=10  #local declaration
    print("inside the function:",n)
                                        
display()
print("outside the function:",n)
'''
'''
def display():
    global n #by using the global keyword we can acces it outside the function
    n=10 
    print("inside the function:",n)
                                        
display()
print("outside the function:",n)
'''
'''
 by using the global keyword 
 we can acces it outside the function
 ##but if ur passing the arg within the function 
 we shldnt use the global keyword inside and declare the arg
 it throws an error-> name 'n' is parameter and global
 '''
'''
def display():
    global n 
    n+=10 
    print("inside the function:",n)
n = 10                           
display()
print("outside the function:",n)
'''
'''
#nested function  =>we use nonlocal only for inside function 
# not entire function within local
def display():
    course = "PFS"
    def update():
        nonlocal course
        course="JFS"
        print("inner function:",course)
    update()
    print("outer function:",course)
display()
'''
'''
##if we use built in methods and assign value it will be taken as a variable
##methods shld be used as methods not as variable 
##if we use as variable it loss its fuction and act as a variable 
'''
'''
l = [1,2,3,4,5]
print(max(l))  #5 it is used as a builtin methon and peform the function
max = 30       #30 it just act as variable 
print(max)
'''
#local scope → variable works only inside the function where it is created.
#global scope → variable can be accessed inside and outside functions.