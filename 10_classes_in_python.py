# here we will understand class concept....
# we will use attack example to understand this....


class Enemy:
    atkl = 60
    atkh = 80

    def getAtk(self):
        print(self.atkl)


enemy1 = Enemy()
enemy1.getAtk()

enemy2 = Enemy()
enemy2.getAtk()
