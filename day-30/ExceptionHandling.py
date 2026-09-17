'''try:
    print(10/10)
except ZeroDivisionError:
    print("Unable to divide a number wih zero")
else:
    print("No errors")
finally:
    print("End of the program")
    

try:
    d={1:1,2:2,3:3}
    print(d[4])
    l=[1,2,3,4]
    print(l[5])
    print('a'+7)
    a = int(input("Enter the amount: "))
    print(n)
    print(10/10)

except NameError:
    print("var is not defined")
except ValueError:
    print("Enter the proper value")
except TypeError:
    print("Enter the same data type ")
except IndexError:
    print("index out of range")
except KeyError:
    print("key is not present")
except ZeroDivisionError:
    print("unable to divide a number with zero")
else:
    print("No Errors")
finally:
    print("End of the program")


  
try:
    d={1:1,2:2,3:3}
    print(d[4])
    l=[1,2,3,4]
    print(l[5])
    print('a'+7)
    a = int(input("Enter the amount: "))
    print(n)
    print(10/10)
except Exception as e:
    print("Error Occured:",e)
else:
    print("No Errors")
finally:
    print("End of the program")

    
    

try:
    d={1:1,2:2,3:3}
    print(d[4])
    l=[1,2,3,4]
    print(l[5])
    print('a'+7)
    a = int(input("Enter the amount: "))
    print(n)
    print(10/10)
except (NameError,ValueError,TypeError,IndexError,KeyError,ZeroDivisionError)as e:
    print("Error Occured:",e)
else:
    print("No Errors")
finally:
    print("End of the program")
'''
try:
    amount = int(input("Enter the amount: "))
    if amount<0:
        raise Exception("Amount needs to be greater than 0")
except Exception as e:
    print("Error occured:" ,e)
else:
    print("No Errors")
finally:
    print("End of the program")