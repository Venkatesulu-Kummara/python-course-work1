Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#INT FLOAT COMPLEX STR LIST TUPLE SET DICT BOOL
a = input()
codegnan
a
'codegnan'
a = input()
1234
a
'1234'
a = input("enter the value")
enter the value 234455677
a
' 234455677'
marks = input("enter the marks:")
enter the marks:90
marks
'90'
marks = int(input("enter the marks:"))
enter the marks:90
marks
90
price = float(input("enter the price"))
enter the price 87.40
price
87.4
cgpa = float(input("enter the cgpa:"))
enter the cgpa:9.56
cgpa
9.56
names = input("enter the names:")
enter the names: usha niha prani
names
' usha niha prani'
names.split()
['usha', 'niha', 'prani']
names.split(',')
[' usha niha prani']
course = 'python-java-c-c++'
course
'python-java-c-c++'
course.split()
['python-java-c-c++']
course.split(',')
['python-java-c-c++']
course.split('-')
['python', 'java', 'c', 'c++']
names = input("enter the numbers:").split()
enter the numbers:usha dumkuu
names
['usha', 'dumkuu']
names = tuple(input("enter the names:").split())
enter the names:dumki pami
names
('dumki', 'pami')
('dumki', 'pami')
('dumki', 'pami')
names = set(input("enter the names:")split())
SyntaxError: invalid syntax. Perhaps you forgot a comma?
names = set(input("enter the names:").split())
enter the names:pathu anu
names
{'anu', 'pathu'}
marks = input().split()
12 34 56 7 8 9
marks
['12', '34', '56', '7', '8', '9']
marks
['12', '34', '56', '7', '8', '9']
map(int,marks)
<map object at 0x0000017508CC4340>
list(map(int,marks))
[12, 34, 56, 7, 8, 9]
marks = list(map(int,input("enter the marks").split()))
enter the marks 90 80 70 60 50
marks
[90, 80, 70, 60, 50]
marks = tuple(map(int,input("enter the marks").split()))
enter the marks 5 6 7 8 
marks
(5, 6, 7, 8)
marks = set(map(int,input("enter the marks").split()))
enter the marks 70 30 68 
marks
{68, 70, 30}
marks = list(map(float,input("enter the marks").split()))
enter the marks 89 64 73 
marks
[89.0, 64.0, 73.0]
marks = tuple(map(float,input("enter the marks").split()))
enter the marks 78 45 63 
marks
(78.0, 45.0, 63.0)
marks = set(map(float,input("enter the marks").split()))
enter the marks 89 65 43
marks
{65.0, 89.0, 43.0}
price  = list(map(float,input("enter the prices").split()))
enter the prices 89.90 83.45
price
[89.9, 83.45]
price  = tuple(map(float,input("enter the prices").split()))
enter the prices 39.22 64.3 857.333
price
(39.22, 64.3, 857.333)
price  = set(map(float,input("enter the prices").split()))
enter the prices 45.5 46.37 938.9
price
{938.9, 45.5, 46.37}
a,b = [1,2]
a
1
b
2
a,b,c = (1,12.3,"str")
a
1
b
12.3
c
'str'
email,password = input("enter the email,password:").split()
enter the email,password: ushavms@gmail.com usha@123
email
'ushavms@gmail.com'
pass
password
'usha@123'
name,marks = input("enter the name and marks:").split())
SyntaxError: unmatched ')'
name,marks = input("enter the name and marks:").split()
enter the name and marks: usha 80
name
'usha'
marks
'80'
int(marks)
80
a,b,c = list(map(int,input().split()))
23 45 67
>>> a
23
>>> b
45
>>> c
67
>>> status = eval(input())
True
>>> status
True
>>> type(status)
<class 'bool'>
>>> status = eval(input())
2+3j
>>> type(status)
<class 'complex'>
>>> status = eval(input())
[1,2,3,4]
>>> staus
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    staus
NameError: name 'staus' is not defined. Did you mean: 'status'?
>>> status
[1, 2, 3, 4]
>>> status = eval(input())
(2,3,4,5)
>>> status
(2, 3, 4, 5)
>>> type(status)
<class 'tuple'>
>>> status = eval(input())
{2,3,4,5}
>>> status
{2, 3, 4, 5}
>>> type(status)
<class 'set'>
>>> status  = eval(input())
{1:2 ,2:3, 4:5}
>>> status
{1: 2, 2: 3, 4: 5}
>>> type(status)
<class 'dict'>