#constructor is a special method tht is going to call automatically ("__init__"=>constructor)

class Instagram:

    def __init__(self,username,password):
        self.username= username
        self.password = password
        print(f"welcome to Instagram {self.username}")
radha = Instagram('sita','765467')
krishna = Instagram('krishna','7656789')
kali = Instagram('kali','5675856865')