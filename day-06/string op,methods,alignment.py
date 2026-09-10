Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
S = "CODEGNAN"
S
'CODEGNAN'
S = ' '
S
' '
a = 'python'
b = ' programming'
a+b
'python programming'
fname = 'usha'
lname = 'rani'
fname + lname
'usharani'
a
'python'
S*10
'          '
a*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
'usharani'*20
'usharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharaniusharani'
'Lu dum' *50
'Lu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dumLu dum'
names
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    names
NameError: name 'names' is not defined. Did you mean: 'fname'?
name = 'usha niha prani pami pathu ali anu kavi ragu'
name
'usha niha prani pami pathu ali anu kavi ragu'
names = 'usha niha prani pami pathu ali anu kavi ragu'
names
'usha niha prani pami pathu ali anu kavi ragu'
names[:5]
'usha '
names[5:8]
'nih'
names[10:15]
'prani'
names[16:20]
'pami'
names[21:26]
'pathu'
names[:-4]
'usha niha prani pami pathu ali anu kavi '
names[-5]
' '

names[-5:]
' ragu'
names[:8]
'usha nih'
l= 'codegnan'
l[3]
'e'
l[-1]
'n'
l[-3]
'n'
l[5]
'n'
l[-7]
'o'
'usha' in names
True
'rani' in names
True
'ranjith' not in name
True
name[::-6]
'uvauinhs'
len(names)
44
ord('b')
98
ord('x')
120
ord('c')
99
chr('20')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    chr('20')
TypeError: 'str' object cannot be interpreted as an integer
chr(20)]
SyntaxError: unmatched ']'
chr(20)
'\x14'
chr(60)
'<'
chr(10)
'\n'
chr(100)
'd'
max()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    max()
TypeError: max expected at least 1 argument, got 0
sorted(names)
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'g', 'h', 'h', 'h', 'i', 'i', 'i', 'i', 'i', 'k', 'l', 'm', 'n', 'n', 'n', 'p', 'p', 'p', 'r', 'r', 's', 't', 'u', 'u', 'u', 'u', 'v']
max(names)
'v'
min(names)
' '
#case conversions string methods
s = " python programming langugage "
s.upper()
' PYTHON PROGRAMMING LANGUGAGE '
s.lower()
' python programming langugage '
s.capitalize()
' python programming langugage '
s.swap case()
SyntaxError: invalid syntax
s.title()
' Python Programming Langugage '
s.swapcase()
' PYTHON PROGRAMMING LANGUGAGE '
s.swapcase()
' PYTHON PROGRAMMING LANGUGAGE '
#foramttingg
s.center(50,'-')
'---------- python programming langugage ----------'
s.center(40,'*')
'***** python programming langugage *****'
s.center(30,'.')
' python programming langugage '
>>> s.ljust(20,'*')
' python programming langugage '
>>> s.ljust(60,'*')
' python programming langugage ******************************'
>>> s.rjust(60,'_')
'______________________________ python programming langugage '
>>> '123'.zfill(5)
'00123'
>>> '57'.zfill(10)
'0000000057'
>>> # find rfind index
>>> s.find('python')
1
>>> s.find('g')
11
>>> s.rfind('p')
8
>>> s.rfind('g')
27
>>> s.index('o')
5
>>> s.find('w')
-1
>>> s.replace('o','1')
' pyth1n pr1gramming langugage '
>>> s.replace('m','2')
' python progra22ing langugage '
>>> s.replace('python','java')
' java programming langugage '
>>> s.maketrans('aeiou','#@$&*')
{97: 35, 101: 64, 105: 36, 111: 38, 117: 42}
>>> s.translate(s.maketrans('aeiou','#@$&*'))
' pyth&n pr&gr#mm$ng l#ng*g#g@ '
>>> text = "hello 😁"
>>> text.encode()
b'hello \xf0\x9f\x98\x81'
>>> text.decode()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> b'hello \xf0\x9f\x98\x81'.decode()
'hello 😁'