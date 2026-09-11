from abc import ABC, abstractmethod

class Payment(ABC):

    def source(self):
        print("Scanner/upid/mobile number")
    def amount(self):
        print("Enter the amount")
    def bank(self):
        print("Select the bank")
    def pin(self):
        print("Enter the pin")
    @abstractmethod
    def  paymentprocess(self):
        print("Payment process ")
        pass
    def paymentstatus(self):
        print("Payment Success/Fail")

class HDFC(Payment):
    def  paymentprocess(self):
        print("Payment process through HDFC bank ")

class PNB(Payment):
    def  paymentprocess(self):
        print("Payment process through PNB bank")

class SBI(Payment):
    def  paymentprocess(self):
        print("Payment process through SBI bank ")

robot = HDFC()
robot.source()
robot.amount()
robot.bank()
robot.pin()
robot.paymentprocess()
robot.paymentstatus()

jaya = PNB()
jaya.source()
jaya.amount()
jaya.bank()
jaya.pin()
jaya.paymentprocess()
jaya.paymentstatus()

dum = SBI()
dum.source()
dum.amount()
dum.bank()
dum.pin()
dum.paymentprocess()
dum.paymentstatus()

