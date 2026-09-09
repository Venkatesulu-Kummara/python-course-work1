Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arthimatic operators
a=10
b=5
a+b
15
a-b
5
a*b
50
a/2
5.0
b/2
2.5
a//2
5
b//2
2
9/2
4.5
16/3
5.333333333333333
16//3
5
a%2
0
17%2
1
17/2
8.5
17//2
8
a**2
100
b***5
SyntaxError: invalid syntax
b**4
625
#comparision operator
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
#ASSIGNMENT OPERATOR
a += 20
a
30
b -= 3
b
2
a *= 100
a
3000
b /= 2
b
1.0
a %=5
a
0
a **=4
a
0
a += 500
a
500
a **= 2
a
250000
#RELATIONAL OR LOGICAL
email = True
password = False
email and password
False
login = True
login = False
display_products = True
login or display_products
True
's' in 'aeiou'
False
's' not in 'aeiou'
True
7%==0 and 3%==0
SyntaxError: invalid syntax
7 %== 0 and 3 %== 0
SyntaxError: invalid syntax
7%2 == 0 and 3%2 ==0
False
5%2 ==0 and 9%2==0
False
4%2 == 0 and 6%2 == 0
True
3%2 == 0
False
not 3%2 ==0
True
#MEMBERSHIP OPERATIONS
s = 'python programming'
a in s
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a in s
TypeError: 'in <string>' requires string as left operand, not int
'a' in s
True
'c++' not in s
True
'program' in s
True
l = [1,2,3,4]
3 in l
True
5 in l
False
5 not in l
True
4 not in l
False
t = (2,3,4,5)
2 not in t
False
3 in t
True
5 in t
True
'abc' not in t
True
s = {3,6,7,8}
3 in s
True
7 in s
True
9 in s
False
'people' in s
False
'waste' not in s
True
data = { 'name' : 'usha' , 'course' : 'pfs' , 'batch' = 65}
SyntaxError: ':' expected after dictionary key
data = {'name' : 'usha' , 'course' : 'pfs' , 'batch': 65 }
name in data
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    name in data
NameError: name 'name' is not defined
data
{'name': 'usha', 'course': 'pfs', 'batch': 65}
name in data
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    name in data
NameError: name 'name' is not defined
>>> 'name'
'name'
>>> 'name' in data
True
>>> 65 in data'
SyntaxError: unterminated string literal (detected at line 1)
>>> 65 in data
False
>>> 'course' in data
True
>>> #IDENTITY OPERATOR
>>> l = [1,2,3,4,5]
>>> m = [1,2,3,4,5]
>>> id(l)
2594650218048
>>> id(m)
2594651840832
>>> l == m
True
>>> l is m
False
>>> n = m
>>> n is m
True
>>> m is n
True
>>> n is not l
True
>>> #BITWISE OPERARTOR
>>> 11 & 12
8
>>> 11 | 12
15
>>> 11 ^ 12
7
>>> 2 << 2
8
>>> 2 << 3
16
>>> 2 <<4
32
>>> 16 >> 2
4
