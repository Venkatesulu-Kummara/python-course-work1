Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
= RESTART: C:\Users\USHA\OneDrive\Desktop\python-course-work\day 2\keywords.py =
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
>>> a=b=c=10
>>> a,b,c=10,20,30
>>> b
20
>>> b=30
>>> b
30
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> c
30
>>> b
30
>>> a,b,c
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a,b,c
NameError: name 'a' is not defined
>>> b,c
(30, 30)
>>> del c
>>> c
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> b
30
>>> a=b=c=20
>>> a
20
>>> b
20
c
20