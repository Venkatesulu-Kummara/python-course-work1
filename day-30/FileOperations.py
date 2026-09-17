'''file = open('demo.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()

with open(' day-30/demo.txt','r')
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()


with open('demo.txt','w')as file:
    file.write("hello world")



with open('demo.txt','w')as file:
    file.write("\nfile operations")

    '''
with open('demo.txt','a+')as file:
    file.write("\nfile operations")
    file.seek(0)
    print(file.read())
