#for printing them in reverse order just write print after the recursion
'''
def display(n):
    if n==11:
        return
    display(n+1)
    print(n)
display(1)
'''
'''
def display(s,n):
    if n==len(s):
        return
    display(s,n+1)
    print(s[n],end = '')
display("codegnan",0)
'''
'''
def display(s,indx,w):
    if len(s)-w+1 == indx:
        return
    print(s[indx:indx+w])
    display(s,indx+1,w)
s = input("Enter the string:")
w = int(input("Enter the width:"))
display(s,0,w)
'''
'''
def display(l,indx):
    if indx == len(l):
        return 0
    return l[indx]+display(l,indx+1)
l=[2,3,4,5,6]
print(display(l,0))
'''
'''
def display(l):
    if l==0:
        return 0
    return l%10 + display(l//10)
  
l=35678
print(display(l))
'''
'''
def display(l):
    if l==1:
        return 1
    return l%10 * display(l//10)
  
l=35678
print(display(l))

'''
'''
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(6))
print(factorial(5))
print(factorial(4))
'''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))