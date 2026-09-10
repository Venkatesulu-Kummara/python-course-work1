#while loop syntax
'''
i = 1
while i<=10:
    print(i)
    i+=1
    '''
'''
i= 10
while i>0:
    print(i)
    i-=1
    '''
'''
i = 5
while i<=50:
    print(i)
    i+=5
     '''
'''
s ='while loop'
i = 0
while i<len(s):
    print(s[i])
    i+=1
     '''
'''
s ='while loop'       #string
i = len(s)-1
while i>=0:
    print(s[i])
    i-=1
     '''
'''
l=[5467,8975,9876,9453]  #list
i=0
while i<len(l):
    print(l[i])
    i+=1
     '''
'''
t=(5467,8975,9876,9453)  #tuple
i=0
while i<len(t):
    print(t[i])
    i+=1
      '''
    #no set dict can iterate
'''
n = 8765
while n>0:
    print(n%10)
    n//=10
      '''
'''
n = 88976545
sumofdigits = 0
while n>0:
    sumofdigits += n%10
    n//=10
print("sum of digits:",sumofdigits)
  '''
'''
n = 88976545
product = 1
while n>0:
    product *= n%10
    n//=10
print("product of digits:",product)
 '''
''' 
n = 34567
rev = 0
while n>0:
    rem = n%10                                                        #rem reminder rev reverse
    rev = rev*10+rem
    n=n//10
print(rev)   
'''
'''
n = 34567
sum = 0
while n>0:
    rem = n%10 
    if rem%2 ==0:
        sum +=rem                                                     
    n=n//10
print(sum)   '''

'''
l = [2,3,4,5,2,0,0,0,0,8,7,0,9,7,0,8,6,5,0,6,0]
i = 0
while i<len(l):
    if l[i]==0:
        l.remove(0)
    else:
        i+=1
print(l)
''' 
'''
l = [2,3,4,5,2,0,0,0,0,8,7,0,9,7,0,8,6,5,0,6,0]
while 0 in l:
    l.remove(0)
print(l)
'''
l = [6,3,4,5,6,7,8,9,10,23,45,67]
i = 0
j = len(l)-1
while i<=j:
    if i == j:
        print(l[i]) 
    else:
        print(l[i]+l[j])
    i+=1
    j-=1