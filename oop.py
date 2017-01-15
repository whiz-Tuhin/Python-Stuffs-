class FirstClass:
    var1 = "Hey i am var"
    def funct_var(self,n):
        for i in range(1,n+1):
            print i+1


firstob = FirstClass()
print firstob.var1

print firstob.funct_var(5)


class Mom:
    var1 = "Hey i am your mom"
    def  namesake(self,name):
        print "Hey %s i am your mom" % name

class Dad:
    var2 = "Hey i am your dad"
    def  namesake2(self,name):
        print "Hey %s i am your dad" % name

"""Me class is inheriting traits from multiple classes"""
class Me(Mom,Dad):
    pass

myob = Me()

print myob.var1
print myob.namesake('tuhin')

print myob.var2
print myob.namesake2('nalin')

class cons:
    var = "Constructor demo"
    def __init__(self):
        print "I am inside a constructor"
        print "I am feeling good"

cob = cons()
print cob.var
