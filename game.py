class Person:

    life = 3

    def attack(self):
        print "i'm hurt!"
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print "I am dead!"
        else:
            print str(self.life) + " Life Left"


p1 = Person()
p1.attack()
p1.attack()
p1.check_life()

p2 = Person()
p2.check_life()
