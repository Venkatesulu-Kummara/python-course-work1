# forloop to iterate the sequence str list tuple set dict range 
# syntax: for var in sequence:
'''
s = 'python programming'
for i in s:
    print(i) 

    
l = [1,2,3,4,5]
for num in l:
    print(num)
    

price = (536,456,286,986,1000)
for prices in price:
    print(prices)
   
s = {'apple','banana','mango','grapes'}
for fruit in s:
    print(fruit)
    
d = {'name':'prabhs','age':22,'city':'delhi'}
for i in d:
    print(i,d[i])
 '''

#range is going to give the numerical values
#range syntax: range(start,stop,step):(0,,1)
'''
for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)
  
for i in range(5,101,5):
    print(i)
    
for i in range(5,0,-1):
    print(i)    
      
for i in range(19,0,-2):
    print(i)

#for index we use range but its not applicale for set and dict but we can use for str list and tuple

s = [2,3,4,5]
for i in range(len(s)):
    print(i,s[i])

s = [2,3,4,5]
for i in range(len(s)):
    print(i,s[i])
    
s = (234,3334,4333,5333)
for i in range(len(s)):
    print(i,s[i])

#anumerate is used to get the sequence numbe and value in tuple format (str list tuple set dict)
s = 'python programming'
for i in enumerate(s):
    print(i)

s = (234,3334,4333,5333)
for i in enumerate(s):
    print(i[0],i[1])
  
d = {1:2,2:4,3:6,4:8,5:10}
for i in enumerate(d):
    print(i[0],i[1])
 
#break is used to terminate the loop continue is used to skip the loop
for i in range(1,11):
    if i==5:
        break
    print(i)
    
for i in range(1,11):
    if i==5:
        continue
    print(i)
 
#if there is no break encounterd inside the else block is executed
# for with else is used when we use break
for i in range(1,11):
    if i==15:
        break
    print(i)
else:
    print("End of the Loop")


l = [12,13,14,15,16,17,18]
n = 26
for i in l:
    if i == n:
        print(n,"found")
        break
else:
    print(n,"Not found")

    
pin = 1234

for i in range(5):
    epin = int(input("Enter the pin:"))
    if epin == pin:
        print("Unlock Phone")
        break
    else:
        print("invalid pin")
else:
    print("Try after 30 seconds")
'''
n = 19
for i in range(2,n):
    if n%i == 0 :
        print("Not a prime number")
        break
else:
    print("prime number")