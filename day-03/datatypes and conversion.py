Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = 20
>>> type(a)
<class 'int'>
>>> b = 20.5
>>> type(b)
<class 'float'>
>>> c = (12+6J)
>>> type(c)
<class 'complex'>
>>> #str list tuple
>>> s = 'CODEGNAN'
>>> type(s)
<class 'str'>
>>> id(s)
2072228666352
>>> s='aaaaaaa'
>>> type(S)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined. Did you mean: 's'?
>>> type(s)
<class 'str'>
>>> l =[1,2,3,4,5,6]
>>> type(l)
<class 'list'>
>>> id(l)
2072228516032
>>> t = (1,2,3,4,5)
>>> type(t)
<class 'tuple'>
>>> t
(1, 2, 3, 4, 5)
>>> t = (1, 12.3, 4,'c')
>>> t
(1, 12.3, 4, 'c')
>>> #set dict
>>> s = {80,40,50,60,90,20,10}
>>> s
{80, 50, 20, 90, 40, 10, 60}
>>> id(s)
2072227998944
s.add(20)
s
{80, 50, 20, 90, 40, 10, 60}
s.add(100)
s
{80, 50, 20, 90, 100, 40, 10, 60}
id(s)
2072227998944
a = {1,12.3,'str'}
a
{1, 12.3, 'str'}
set(s)
{100, 40, 10, 80, 50, 20, 90, 60}
type(s)
<class 'set'>
d = {'productname' = 'xyz' ,'price' = 200, 'stock' = True}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
d = {'productname' = 'xyz' ,'price' = 200, 'stock' = True}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
d = {'productname:'xyz' ,'price': 200, 'stock': True}
     
SyntaxError: unterminated string literal (detected at line 1)
d = {'productname' : 'xyz' ,'price' : 200, 'stock' : True}
     
s={1,2,3,4}
     
s= frozenset({2,2,4,5,5})
     
s
     
frozenset({2, 4, 5})
a=True
     
b=False
     
type(a)
     
<class 'bool'>
a=()
     
b=[]
     
c={}
     
s=''
     
d=None
     
type(d)
     
<class 'NoneType'>
# type casting
     
a = 10
     
float(a)
     
10.0
str(a)
     
'10'
complex(a)
     
(10+0j)
bool(a)
     
True
list(a)
     
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
     
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
     
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
     
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
f = 20.3
     
int(f)
     
20
complex(f)
     
(20.3+0j)
bool(f)
     
True
str(f)
     
'20.3'
c = 12+3j
     
int(c)
     
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
str(c)
     
'(12+3j)'
bool(c)
     
True
float(c)
     
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
s='codegnan'
     
a='3456'
     
int(s)
     
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
int(a)
     
3456
float(a)
     
3456.0
bool(s)
     
True
list(s)
     
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(s)
     
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(s)
     
{'n', 'e', 'a', 'd', 'g', 'o', 'c'}
dict(s)
     
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
l=[1,3,4,5,6,7,8]
     
int(l)
     
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
     
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
     
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
     
'[1, 3, 4, 5, 6, 7, 8]'
tuple(l)
     
(1, 3, 4, 5, 6, 7, 8)
set(l)
     
{1, 3, 4, 5, 6, 7, 8}]
bool(l)
True
dict
<class 'dict'>
dict(l)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
tuple=(1,2,3,4,5)
str(t)
"(1, 12.3, 4, 'c')"
list(t)
[1, 12.3, 4, 'c']
set(t)
{'c', 1, 12.3, 4}
bool(t)]
SyntaxError: unmatched ']'
bool(t)
True
dict(t)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
int(t)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
dict={1:1,2:2,3:3}
str(dict)
'{1: 1, 2: 2, 3: 3}'
list(dict)
[1, 2, 3]
tuple(dict)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    tuple(dict)
TypeError: 'tuple' object is not callable
tuple(dict)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    tuple(dict)
TypeError: 'tuple' object is not callable
del tuple
tuple(dict)
(1, 2, 3)
bool(dict)
True
bool=True
int(bool)
1
float(bool)
1.0
str(bool)
'True'
list(bool)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    list(bool)
TypeError: 'bool' object is not iterable