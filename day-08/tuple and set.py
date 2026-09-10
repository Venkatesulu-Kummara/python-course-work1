Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
t = ()
t = tuple()
t = (1,2,3,4)
t
(1, 2, 3, 4)
t = (1)
1
1
t
1
t = (1, )
t
(1,)
t = (1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t = (1,23.4,"str",[1,2],(1,2,3),{1,2,3},{1:1,2:2},True)
t
(1, 23.4, 'str', [1, 2], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
type(t)
<class 'tuple'>
#TUPLE OPERATIONS
#concatination repetation indexing sclicing membership
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3)*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 23.4, 'str', [1, 2], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[1]
23.4
t[4]
(1, 2, 3)
t[-1]
True
t[-3]
{1, 2, 3}
t[2]
'str'
t[3:2]
()
t[3:7]
([1, 2], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
t[-3:-1]
({1, 2, 3}, {1: 1, 2: 2})
t[-3:-1:1]
({1, 2, 3}, {1: 1, 2: 2})
t
(1, 23.4, 'str', [1, 2], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
23.4 in t
True
'str' in t
True
True in t
True
False in t
False
t[-1:3:-1]
(True, {1: 1, 2: 2}, {1, 2, 3}, (1, 2, 3))
t = (23,34,667,88,66,33,66,33,89)
t
(23, 34, 667, 88, 66, 33, 66, 33, 89)
sorted(t)
[23, 33, 33, 34, 66, 66, 88, 89, 667]
max(t)
667
min(t)
23
len(t)
9
t
(23, 34, 667, 88, 66, 33, 66, 33, 89)
t.index(34)
1
t.count(33)
2
t.count(88)
1
t.index(89)
8
sum(t)
1099
all((1,2,3))
True
any(0,2,3,5,7)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    any(0,2,3,5,7)
TypeError: any() takes exactly one argument (5 given)
any((0,2,3,5,7))
True
any((00,2,3,5,7))
True
all((00,2,3,5,7))
False
t = 1,2,3
t
(1, 2, 3)
a,b,c = t
a
1
b
2
c
3
#SET
s = set() #empty set is given as set() not set{}
type(s)
<class 'set'>
s = {1,2,3,4,5,6,134566,34566,8876}
s = {1,1,1,1,1}
s
{1}
s = set()
s.add(1)
s.add(23.4)
s.add("ush")
s.add((1,2,3))
#cant add list ,set ,dict into set
s.add([2,34])
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s.add([2,34])
TypeError: unhashable type: 'list'
s.add({3,4,5})
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.add({3,4,5})
TypeError: unhashable type: 'set'
s.add({1:1,2:3,})
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.add({1:1,2:3,})
TypeError: unhashable type: 'dict'
s.add(True)
s
{1, 'ush', (1, 2, 3), 23.4}
#set operations
#no concatenantion , repetation,indexing ,sclicing
#consist of membership operation , for concatenation we use union not +
# union | ,intersection &,difference -,symmetric difference ^ ,subset ,superset, disjoin
a = {1,2,3,4,5}
b = {3,5,7,8,9}
2 in a
True
10 not in a
True
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
b - a
{8, 9, 7}
a ^ b
{1, 2, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5}
{1}<=a
True
{1,2,3}<= a
True
{1,7,8,9}<=a
False
a>={1,2}
True
a>={3,5,6}
False
a>={2,4,5}
True
m = {1,2,3}
n = {4,5,6}
n.isdisjoint(m)
True
a.isdisjoint(n)
False
# sum max min sorted all any copy len
a ={12,34,5,6,78,09}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a ={12,34,5,6,78,9}
a
{34, 5, 6, 9, 12, 78}
sorted(a)
[5, 6, 9, 12, 34, 78]
len(a)
6
min(a)
5
max(a)
78
sum(a)
144
a = {1,2,3}
b = a
a
{1, 2, 3}
b
{1, 2, 3}
c = a.copy()
a.add(20)
c
{1, 2, 3}
>>> any({True,0,1,2,3,()})
True
>>> all({1,12,5,78})
True
>>> any({0,''})
False
>>> c.add(7)
>>> c
{1, 2, 3, 7}
>>> #cant modify set but we can add or delete
>>> a.add(100)
>>> a
{1, 2, 3, 100, 20}
>>> a.add(200)
>>> a
{1, 2, 3, 100, 200, 20}
>>> #to add multiple elements we use update
>>> a.update({19,45,67,34,89})
>>> a
{1, 2, 3, 100, 34, 67, 200, 45, 19, 20, 89}
>>> a.pop()
1
>>> a.pop()
2
>>> a.pop() # it deletes the element randomly
3
>>> a.remove(100) #removes the particular value
>>> a
{34, 67, 200, 45, 19, 20, 89}
>>> #we use discard if its not there or already removed it wont throw any error
>>> a.discard(100)
>>> a
{34, 67, 200, 45, 19, 20, 89}
>>> #frozen set is immutable set cant add cant delet
>>> a = frozenset(1,2,3)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    a = frozenset(1,2,3)
TypeError: frozenset expected at most 1 argument, got 3
>>> KeyboardInterrupt
>>> a = frozenset({1,2,3})
>>> a
frozenset({1, 2, 3})