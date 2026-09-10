Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict
d = {}
type(d)
<class 'dict'>
d = {1:4 ,5:7,8:9}
d
{1: 4, 5: 7, 8: 9}
d = {}
d[1] = 1
d[12.3] = 1
d[2+3j] = 1
d[[1,2,3]] = 1
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d[[1,2,3]] = 1
TypeError: unhashable type: 'list'
# dict cant allow list set dic inside key
d[(1,2,3)] = 1
d["str"] = 1
d[True] = 1
#it wont allow set and dic as keys
d[{2,3,4}] = 1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d[{2,3,4}] = 1
TypeError: unhashable type: 'set'
d[{1:2,3:4}]  = 1
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d[{1:2,3:4}]  = 1
TypeError: unhashable type: 'dict'
# it allows only immutable datatypes in keys
#but in values it can have any datatype
d
{1: 1, 12.3: 1, (2+3j): 1, (1, 2, 3): 1, 'str': 1}
d[False] = 1
d
{1: 1, 12.3: 1, (2+3j): 1, (1, 2, 3): 1, 'str': 1, False: 1}
d[1] = 1
d[2] = 2.3
d[3] = 2+3i
SyntaxError: invalid decimal literal
d[3] = 2+6j
d[4] = [1,2,3]
d[5] = "str"
d[6] = (2,3,4)
d[7] = {6,7,8}
d[8] = False
d[9] = frozenset[{4,5,6}]
d[10] = {1:2,4:5,8:9}
d[11] = None
d
{1: 1, 12.3: 1, (2+3j): 1, (1, 2, 3): 1, 'str': 1, False: 1, 2: 2.3, 3: (2+6j), 4: [1, 2, 3], 5: 'str', 6: (2, 3, 4), 7: {8, 6, 7}, 8: False, 9: frozenset[{4, 5, 6}], 10: {1: 2, 4: 5, 8: 9}, 11: None}
d = {}
d[1] = 2
d
{1: 2}
d[1] = 3
d
{1: 3}
#we dont have concatination indexing repetation sclicing
#we have membership it works only for keys but we can acces the value with help of keys ,to handle the error we have get method so no error occurs but it execute
d = {'name' : 'abc' ,'course' : 'pfs','batch' : 65}
d
{'name': 'abc', 'course': 'pfs', 'batch': 65}
'abc' in d
False
'name' in d
True
'pfs' in d
False
d[name]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    d[name]
NameError: name 'name' is not defined
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
d['name']
'abc'
d['course']
'pfs'
d['age']
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    d['age']
KeyError: 'age'
d.get('age')
d.get('name')
'abc'
d.get('course')
'pfs'
d.get('age','key is not found')
'key is not found'
id(d)
2063835152320
d
{'name': 'abc', 'course': 'pfs', 'batch': 65}
d['age'] = 21
d[phnno] = 99999999999
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d[phnno] = 99999999999
NameError: name 'phnno' is not defined
d['phnno'] = 99999999999
d
{'name': 'abc', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 99999999999}
data.update = ({'email' : 'abc@gmail.com' , 'py' : 2026})
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    data.update = ({'email' : 'abc@gmail.com' , 'py' : 2026})
NameError: name 'data' is not defined
data.update({'email' : 'abc@gmail.com' , 'py' : 2026})
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    data.update({'email' : 'abc@gmail.com' , 'py' : 2026})
NameError: name 'data' is not defined
d.update({'email' : 'abc@gmail.com' , 'py' : 2026})
d
{'name': 'abc', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 99999999999, 'email': 'abc@gmail.com', 'py': 2026}
id(d)
2063835152320
d['py']
2026
d.popitem()
('py', 2026)
d.pop('course')
'pfs'
d.popitem()
('email', 'abc@gmail.com')
del d['batch']
d
{'name': 'abc', 'age': 21, 'phnno': 99999999999}
d.clear()
d
{}
>>> data ={'name': 'abc', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 99999999999}
>>> len(data)
5
>>> data.keys()
dict_keys(['name', 'course', 'batch', 'age', 'phnno'])
>>> data.values()
dict_values(['abc', 'pfs', 65, 21, 99999999999])
>>> data.items()
dict_items([('name', 'abc'), ('course', 'pfs'), ('batch', 65), ('age', 21), ('phnno', 99999999999)])
>>> sorted(data)
['age', 'batch', 'course', 'name', 'phnno']
>>> max(data)
'phnno'
>>> min(data)
'age'
>>> d = {1:1,2:2}
>>> m = d
>>> m[3] = 3
>>> m
{1: 1, 2: 2, 3: 3}
>>> d
{1: 1, 2: 2, 3: 3}
>>> n = d.copy()
>>> n[5] = 5
>>> n
{1: 1, 2: 2, 3: 3, 5: 5}
>>> d
{1: 1, 2: 2, 3: 3}
>>> data
{'name': 'abc', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 99999999999}
>>> #if we use set default if the key is not present in the dict it gonna update
>>> data.setdefault('name',2026)
'abc'
>>> data.setdefault('age',2026)
21
>>> data.setdefault('key',2026)
2026
>>> data
{'name': 'abc', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 99999999999, 'key': 2026}
>>> dict.fromkeys(["python","mysql","java"],0)
{'python': 0, 'mysql': 0, 'java': 0}