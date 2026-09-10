Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l = []
l = list()
type(l)
<class 'list'>
l = [1.12.3,"str",[1,2,3],(2,3,4,5),{2,5,67,9},{1:1,2:2,3:3},6+4j]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l = [13,12.3,"str",[1,2,3],(2,3,4,5),{2,5,67,9},{1:1,2:2,3:3},6+4j]
l
[13, 12.3, 'str', [1, 2, 3], (2, 3, 4, 5), {9, 2, 67, 5}, {1: 1, 2: 2, 3: 3}, (6+4j)]
l = [1,1,1,1,1]
l
[1, 1, 1, 1, 1]
a=[1,2,3]
b=[3,4,5]
a+b
[1, 2, 3, 3, 4, 5]
a*4
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
a = [567,76,13,433,134,234]
a
[567, 76, 13, 433, 134, 234]
a[1]
76
a[5]
234
a[3]
433
a[-1]
234
a[::-1]
[234, 134, 433, 13, 76, 567]
a[:3:-1]
[234, 134]
a[1:4]
[76, 13, 433]
a[1::2]
[76, 433, 234]
a
[567, 76, 13, 433, 134, 234]
76 in a
True
897 in a
False
13 not in a
False
max(a)
567
min(a)
13
sorted(a)
[13, 76, 134, 234, 433, 567]
len(a)
6
a
[567, 76, 13, 433, 134, 234]
id(a)
2727634129024
a[3]
433
a.append(29)
a
[567, 76, 13, 433, 134, 234, 29]
a.append(78)
a
[567, 76, 13, 433, 134, 234, 29, 78]
a.extend([2,3,4,5])
a
[567, 76, 13, 433, 134, 234, 29, 78, 2, 3, 4, 5]
a.insert(2,50)
a
[567, 76, 50, 13, 433, 134, 234, 29, 78, 2, 3, 4, 5]
a.insert(1,20)
a
[567, 20, 76, 50, 13, 433, 134, 234, 29, 78, 2, 3, 4, 5]
a.pop()
5
a.pop(4)
13
a
[567, 20, 76, 50, 433, 134, 234, 29, 78, 2, 3, 4]
a.remove(78)
a
[567, 20, 76, 50, 433, 134, 234, 29, 2, 3, 4]
del a[2:6]
a
[567, 20, 234, 29, 2, 3, 4]
a.clear()
a
[]
id(a)
2727634129024
a.index(13)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.index(13)
ValueError: 13 is not in list
a.index(20)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.index(20)
ValueError: 20 is not in list
>>> a = [567,76,13,433,134,234]
>>> a.index(134)
4
>>> a
[567, 76, 13, 433, 134, 234]
>>> a.count(76)
1
>>> a = [1,2,3,4]
>>> b = a
>>> b.append(23)
>>> a
[1, 2, 3, 4, 23]
>>> c = a.copy()
>>> c.append(23)
>>> c
[1, 2, 3, 4, 23, 23]
>>> a
[1, 2, 3, 4, 23]
>>> any([1,@,true,false])
SyntaxError: invalid syntax
>>> any([1,uuuu,true,false])
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    any([1,uuuu,true,false])
NameError: name 'uuuu' is not defined
>>> any([1,'us',true,false])
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    any([1,'us',true,false])
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> any([1,True,False])
True
>>> all([1,2,3,4])
True
>>> all([1,True,False])
False
>>> a
[1, 2, 3, 4, 23]
>>> sum(a)
33
>>> a.sort()
>>> a
[1, 2, 3, 4, 23]
a.reverse()
a
[23, 4, 3, 2, 1]