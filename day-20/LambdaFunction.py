#lambda is a fuction without name 
# has only one expression can have multiple arguments
# we dont use def keyword to define a lambda function 
# we use lambda keyword to define a lambda function
'''
syntax:
variable = lambda arguments: expression

wish = lambda name:f'hello welcome to lambda function:{name}'
print(wish('abc'))
print(wish('xyz'))

gst = lambda price: price*0.18
print(gst(1000))
print(gst(5000))

avg = lambda a,b,c:(a+b+c)/3
print(avg(2,5,6))

vowels = lambda a:"vowel" if a in 'aeiouAEIOU' else "consonant"
print(vowels('a'))
print(vowels('b'))

iseven = lambda a: "Even" if a%2==0 else "Odd"
print(iseven(4))
print(iseven(5))

largest = lambda a,b,c: a if a>b and a>c else (b if b>c else c)
print(largest(10,20,30))
print(largest(100,20,30))

#map used to update each element of the list,tuple,set,dict

l = [1,2,3,4,5,6,7,8,9,10]
update = list(map(lambda a:a+10,l))
print(update)

t = (2334,4566,2345,6789,3456)
discount = tuple(map(lambda i: i-i*0.3, t))
print(discount)

#filter used to filter elements from a list,tuple,set,dict based on a condition
l = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda a: a%2==0, l))
print(even)

t = (2334,4566,2345,6789,3456)
discount = tuple(filter(lambda i: i>1000, t))
print(discount)

l =['abc@codegnan.com','abc@yahoo.com','abc@gmail.com','abc@outlook.com']
res = list(map(lambda i: i.split('@')[-1], l))
print(res)

from functools import reduce

l =[4556,2345,4566,7888,3453]
res = reduce(lambda sum,i: sum+i, l)
print(res)

res1 = reduce(lambda sum,i: sum*i, l)
print(res1)

seats = {'s1':True,
         's2':False,
         's3':False,
         's4':True,
         's5':True,
         's6':True}   
res = list(filter(lambda i:seats[i]==True,seats))
print(res)

products = {
    'egg':80,
    'sugar':60,
    'salt':20,
    'butter':40,
    'milk':30
}
res = list(filter(lambda i:products[i]>50,products))
print(res)
'''
products = {
    'egg':80,
    'sugar':60,
    'salt':20,
    'butter':40,
    'milk':30
}
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))