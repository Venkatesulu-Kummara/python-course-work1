# main purpose is to reuse the code 
'''
#single inheritance
class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload status for 24 hrs")

dum = whatsappv1()
dum.message()

sha = whatsappv2()
sha.message()
sha.status()
'''
'''
#multi level inheritance
class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload status for 24 hrs")

class whatsappv3(whatsappv2):
    def groups(self):
        print("you can create groups and talk with multiple people at the same time")

dum = whatsappv1()
dum.message()

sha = whatsappv2()
sha.message()
sha.status()

jaya = whatsappv3()
jaya.message()
jaya.status()
jaya.groups()
'''
'''
#hybrid and multiple inheritance
class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload status for 24 hrs")

class whatsappv3():
    def groups(self):
        print("you can create groups and talk with multiple people at the same time")
class whatsappv4():
    def community(self):
        print("you can group multiple groups at a time")

class whatsappv5(whatsappv2,whatsappv3,whatsappv4):
    def channel(self):
        print("you can post multiple post in a huge crowd ")

jaya = whatsappv5()
jaya.message()
jaya.status()
jaya.groups()
jaya.community()
jaya.channel()
'''
#hierarchical inheritance
class whatsappv1:
    def message(self):
        print("you can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("you can upload status for 24 hrs")

class whatsappv3(whatsappv1):
    def groups(self):
        print("you can create groups and talk with multiple people at the same time")
class whatsappv4(whatsappv1):
    def community(self):
        print("you can group multiple groups at a time")

jaya = whatsappv1()
jaya.message()

shree = whatsappv2()
shree.message()
shree.status()

pooja = whatsappv3()
pooja.message()
pooja.groups()

dum = whatsappv4()
dum.message()
dum.community()