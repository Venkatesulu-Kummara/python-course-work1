Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strip(trimming method)
s = '         Hello    World          '
s.strip()
'Hello    World'
s.lstrip()
'Hello    World          '
s.rstrip()
'         Hello    World'
s.replace('  ','')
' HelloWorld'
s.replace(' ','')
'HelloWorld'
'HelloWorld'
'HelloWorld'

#splitting methods
#joining methods
s = 'python-java-mysql-sql-flask'
s.split('-')
['python', 'java', 'mysql', 'sql', 'flask']
s.split('-',2)
['python', 'java', 'mysql-sql-flask']
s.split('-',3)
['python', 'java', 'mysql', 'sql-flask']
l = '''python
java
mysql
database
'''
1
1
l
'python\njava\nmysql\ndatabase\n'
l.splitlines()
['python', 'java', 'mysql', 'database']
c = ['python', 'java', 'mysql', 'database']
c
['python', 'java', 'mysql', 'database']
''.join(s)
'python-java-mysql-sql-flask'
' '.join(s)
'p y t h o n - j a v a - m y s q l - s q l - f l a s k'
c.split('-')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    c.split('-')
AttributeError: 'list' object has no attribute 'split'
'@'.join(c)
'python@java@mysql@database'
'-'.join(('1','2','3','4'))
'1-2-3-4'
'-'.join({'1','2','3','4'})
'1-2-4-3'
''.join(c)
'pythonjavamysqldatabase'
'-'.join(c)
'python-java-mysql-database'
a=string.py
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a=string.py
NameError: name 'string' is not defined. Did you forget to import 'string'?
a='string.py'
a.partition('.')
('string', '.', 'py')
a = 'string.py.java.png.txt'
a
'string.py.java.png.txt'
a.partition('.')
('string', '.', 'py.java.png.txt')
a.rpartition('.')
('string.py.java.png', '.', 'txt')
>>> a = 'string.png'
>>> a.startswith('str')
True
>>> a.startswith('lists')
False
>>> a.endswith('png')
True
>>> 'pythonv.11'.islower()
True
>>> 'PYTHON23345656'.isupper()
True
>>> 'Python'.isupper()
False
>>> 'Python'.islower()
False
>>> '123334'.isalnum()
True
>>> 'qwbdheuifheskj'.isalpha()
True
>>> '22345adsdh'.isalpha()
False
>>> 'dfvghjgfds'.isalnum()
True
>>> 'Python World'.istitle()
True
>>> 'PYthon worls'.istitle()
False
>>> '            '.isspace()
True
>>> '        hello'.isspace()
False
>>> 'my_value'.isidentifier()
True
>>> 'my_value@'.isidentifier()
False
>>> '328734873'.isdecimal()
True
>>> 'sedbhg64r78438'.isdecimal()
False
>>> '376378689'.isdigit()
True
>>> '7989'.isnumeric()
True