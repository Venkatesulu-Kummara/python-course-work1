#immutabel items => pass by value (int,float,complex,tuple,str,bool)=>changes done only in 
#mutable items=> pass by reference (list,dict,set)=>changes occurs both in and out
'''#int
def display(n):
    n+=4 #14 o/p
    print("inside function:",n)
n=10 #10 o/p
display(n)
print("outer function:",n)
'''
''' #float
def display(n):
    n+=4.9 #15.4 o/p
    print("inside function:",n)
n=10.5 #10.5 o/p
display(n)
print("outer function:",n)
'''
''' #complex
def display(n):
    n+=2 #6+5j
    print("inside function:",n)
n=4+5j  #4+5j
display(n)
print("outer function:",n)
'''
'''
#string
def display(n):
    n+=" lang" # python lang
    print("inside function:",n)
n="python" # python
display(n)
print("outer function:",n)
'''
'''#tuple
def display(n):
    n+=(2,3)   #(1,4,5,6,2,3)
    print("inside function:",n)
n=(1,4,5,6)    #(1,4,5,6)
display(n)
print("outer function:",n)
'''
'''#bool
def display(n):
    n=True
    print("inside function:",n)
n=False
display(n)
print("outer function:",n)
'''
'''#list
def display(n):
    n+=[5,6,7] #[2, 3, 4, 5, 6, 7]
    print("inside function:",n)
n=[2,3,4]  #[2, 3, 4, 5, 6, 7]
display(n)
print("outer function:",n)
'''
'''#set
def display(n):
    n.add(4) #{3, 4, 5, 6}
    print("inside function:",n)
n={3,4,5,6} 
display(n)
print("outer function:",n)
'''
'''#dict
def display(n):
    n[4]=3
    print("inside function:",n)
n={3:4,8:5} 
display(n)
print("outer function:",n)
'''