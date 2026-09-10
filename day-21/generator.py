'''
generator is a special type of function that returns an iterator object 
which we can iterate over one value at a time. 
It is used to create iterators in a simple way. 
A generator function is defined like a normal function 
but whenever it needs to generate a value, it does so with the yield keyword i rather than return. 
If the body of a def contains yield, the function automatically becomes a generator function.
yeild is used to pausing  the function than terminating it.
''' 
'''
def reels():
    data = ['1..100','101..200','201..300','301..400','401..500']
    for i in data:
        yield i

res = reels()
print(next(res))
print(next(res))
print(next(res))
print(next(res))
'''
'''
def countdown():
    yield 5
    yield 4         
    yield 3
    yield 2
    yield 1
res = countdown()
for i in res:
    print(i)
'''
'''
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i

res = factors(6)
for i in res:
    print(i)
'''
def prime(n):
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            yield i
res = prime(20)
for i in res:
    print(i)