# two loops - inner loop(column) outer loop-(row)
#patterns
'''
for row in range(10):
    for col in range(5):
        print(col,end = '')
    print()
'''
'''
for i in range(5):
    for j in range(5):
        print('*',end = '')
    print()
'''
'''
for i in range(5):
    for j in range(5):
        print(j%2,end = '')
    print()
'''
'''
for i in range(5):
    for j in range(5):
        print(i%2,end = '')
    print()
'''
'''
for i in range(5):
    for j in range(5):
        print((i+j)%2,end = '')
    print()
'''
'''
for i in range(5):
    for j in range(5):
        print((i+j),end = '')
    print()
'''
'''
c = 1
for i in range(5):
    for j in range(5):
        print(c,end = '')
        c+=1
    print()
'''
'''
for i in range(5):
    for j in range(i+1):
        print('*',end = '')
    print()
'''
'''
for i in range(5):
    for j in range(5-i):
        print('*',end = '')
       
    print()
'''
'''
n = 5
for i in range(n):
    for space in range(n - i - 1):
        print(' ',end = '')
    for j in range(i+1):
        print('*',end = '')       
    print()
'''
'''
n = 5
for i in range(n):
    for sp in range(i):
        print(' ', end = '')
    for j in range(n-i):
        print('*',end = '')
    print()
'''
'''
n=9
m = n//2
for i in range(n):
    if i <= m:
        for j in range(i+1):
            print('*',end = ' ')
    else:
        for k in range(n-i):
            print('*',end = ' ')
    print()
'''
'''
#optimize in simple way
n=9
m = n//2
for i in range(n):
    if i <= m:
        print('* '*(i+1),end = ' ')
    else:
        print('* '*(n-i),end = ' ')
    print()
'''
'''
n=9
m = n//2
for i in range(n):
    if i <= m:
        print(' '*(m-i),'*'*(i+1),end = ' ')
    else:
        print(' '*(i-m),'*'*(n-i),end = ' ')
    print()
'''
n = 5
num = 1
for i in range(n):
    row = []
    for j in range(n):
        row.append(num)
        num += 1

    if i % 2 == 1:
        row.reverse()

    print(*row)