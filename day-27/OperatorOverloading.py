'''
"Operator overloading is an example of polymorphism."
"One name or interface can have different forms or behaviors"
Operator overloading is a feature of Python that allows us to define 
how operators behave when they are used with objects." 
It is implemented using special methods/magic methods such as __add__(), __sub__(), and __eq__()."
'''
class Number:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, other):
        return self.n + other.n   
    
    def __sub__(self, other):
        return self.n - other.n
    
    def __mul__(self, other):
        return self.n * other.n 
    
    def __truediv__(self, other):
        return self.n / other.n
    
    def __floordiv__(self, other):
        return self.n // other.n
    
    def __mod__(self, other):
        return self.n % other.n
    
    def __pow__(self, other):
        return self.n ** other.n
    
    def __gt__(self, other):
        return self.n > other.n
    
    def __lt__(self, other):
        return self.n < other.n
    
    def __ge__(self, other):
        return self.n >= other.n
    
    def __le__(self, other):
        return self.n <= other.n
    
    def __eq__(self, other):
        return self.n == other.n
    
    def __ne__(self, other):
        return self.n != other.n
    def __str__(self):
        return str(self.n)
        
a = Number(10)
b = Number(20)

print(a+b) 
print(a-b)       
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
print(a)