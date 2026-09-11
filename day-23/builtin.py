'''
import sys 

print(sys.argv)
print(sys.version)
print(sys.path)
print("start")
sys.exit()
print("end")
'''

'''
import platform

print(platform.system())
print(platform.release())
print(platform.processor())
'''
'''
import math

print(math.pi)
print(math.e)
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.gcd(8,12))
print(math.sqrt(36))
print(math.pow(2,3))
'''

'''
# for round function we dont need to import math
print(round(12.000001))
print(round(12.3))
print(round(12.66666666666666))
print(round(12.999999))

import math
print(math.ceil(12.000001))
print(math.ceil(12.3))
print(math.ceil(12.66666666666666))
print(math.ceil(12.45))

print(math.floor(12.002))
print(math.floor(12.3222))
print(math.floor(12.7222222))
print(math.floor(12.0000001))
'''
'''
import random

random.seed(7)
print(random.random())
print(random.randint(10000,999999))
print(random.uniform(1,6))

l = ['r','p','s']
print(random.choice(l))

lang = ['python','css','javascrip','html']
print(random.choices(lang,k=2))

random.shuffle(lang)
print(lang)
'''
'''
text = "python programming"
dict ={}
for i in text:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
'''

from collections import Counter,defaultdict,deque

s = 'python language'
res = Counter(s)
print(res)

products =['sugar','salt','milk']
res = defaultdict(list)
for i in products:
    res[i].append(['des','rev','com'])
print(res)

s = 'python programming'
d = defaultdict(int)
for i in s:
    d[i]+=1
print(d)

l = deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
print(l)

l = deque([])
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.popleft()
l.popleft()
l.append(50)
l.append(60)
print(l)