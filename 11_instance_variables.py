# here we will discuss instance variables...
# again considering the attack example...

class Enemy:

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)


enemy1 = Enemy(40, 60)
enemy1.getAtk()

enemy2 = Enemy(70, 80)
enemy2.getAtk()
