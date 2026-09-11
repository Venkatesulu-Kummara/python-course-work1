'''
super() is a built-in function in Python used to call methods or 
constructors of the parent class from the child class.
It is mainly used in inheritance and method overriding.
super method works only for single level
'''
'''
#single level
class whatsappv1:
    def status(self):
        print("you can upload status for 24 hrs")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("you can add music and u can react")

a = whatsappv1()
a.status()

b = whatsappv2()
b.status()
'''
'''
#if more than single level we use cls method and pass self
class whatsappv1:
    def status(self):
        print("you can upload status for 24 hrs")

class whatsappv2:
    def status(self):
        print("you can add music and u can react")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)                            
        whatsappv2.status(self)
        print("you can add music and u can react")

a = whatsappv3()
a.status()

#whatsapp1 is cls method and we pass self for get the info
 '''