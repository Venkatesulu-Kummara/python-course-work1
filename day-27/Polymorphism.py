#method overloading - same method diff actions (but python dont support it)

#method overriding - same method same parameters different responce 

class Hotstar:
    def __init__(self,name):
        print(f'welocme to the hotstar,{name}----------------------')
    def auth(self):
        print("you can login/register")
    def dashboard(self):
        print("you can see your dashboard")
    def search(self):
        print("you can search")
    def history(self):
        print("you can see history")
    def playcontrollers(self):
        print("you can resume the video")
    def ads(self):
        print("ads wil run")
    def quality(self):
        print("you have limited quality")  
    def access(self):
        print("limited access")
    def device(self):
        print("limited access for login")
    def download(self):
        print("you cant download the video")
        
class premiumhotstar(Hotstar):
    def __init__(self,name):
        print(f'welocme to the hotstar,{name}----------------------')
    def auth(self):
        print("you can login/register")
    def dashboard(self):
        print("you can see your dashboard")
    def search(self):
        print("you can search")
    def history(self):
        print("you can see history")
    def playcontrollers(self):
        print("you can resume the video")
    def ads(self):
        print("no ads")
    def quality(self):
        print("you have high quality")  
    def access(self):
        print("limited access")
    def device(self):
        print("multiple login")  
    def download(self):
        print("you can download the video")

ragu = Hotstar("ragu")
ragu.auth()
ragu.dashboard()
ragu.search()
ragu.history()
ragu.playcontrollers()
ragu.ads()
ragu.quality()
ragu.access()
ragu.device()
ragu.download()

anu = premiumhotstar("anu")
anu.auth()
anu.dashboard()
anu.search()
anu.history()
anu.playcontrollers()
anu.ads()
anu.quality()
anu.access()
anu.device()
anu.download()