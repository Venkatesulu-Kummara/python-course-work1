''' any method we use self 
public = inside cls, childclass, outside
(__)we use double underscore for private = inside cls
(_)we use single underscore for protected = inside cls , childcls, outside(not recommended)
'''

class Instagram:

    def __init__(self,username,password):
        self.username= username
        self.__password = password
        self._post = []
        
    def getpassword(self):
        return self.__password
    
    def setpassword(self,setpassword):
            self.__password = setpassword
    
    @property
    def accesspost(self):
        return self._post
    
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

kali = Instagram('kali','2435566')
print(kali.username)
print(kali.getpassword())
print(kali.accesspost)

kali.username = 'kali_123'
print(kali.username)

kali.setpassword('kali@@123')
print(kali.getpassword())

kali.accesspost = 'python intro'
kali.accesspost = 'strings intro'
kali.accesspost = 'project intro'
print(kali.accesspost)