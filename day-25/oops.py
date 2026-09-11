'''
class Flipcart:
    pass  # pass is used for created an empty block

abc = Flipcart() # we creating an object abc and calling the class function
efg = Flipcart()
hij = Flipcart()
'''
class Flipcart:
    dicount = 30

    @classmethod
    def updatediscount(cls):
      cls.discount = 40
      print("updated Discount:",cls.discount)
    
    def info(self,name,phoneno,address):
      self.name = name
      self.phoneno = phoneno
      self.address = address
      print(f'welcome to Flipcart',self.name)
      
    @staticmethod
    def banner():
      print(f"{Flipcart.discount}% dicount is going,grab the product")
jaya = Flipcart()
jaya.info('abc',8737639848,'hyd')
jaya.updatediscount()
jaya.banner()
virat = Flipcart()
virat.info('abc',8737639848,'banglr')
virat.updatediscount()
virat.banner()
prab = Flipcart()
prab.info('abc',8737639848,'chennai')
prab.updatediscount()
prab.banner()