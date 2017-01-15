# the methods for lists that i have learned are
"""
1.) append
2.) count
3.) extend
4.) index
5.) insert
6.) pop
7.) remove
8.) reverse
9.) len function """


mylist = [54,89,12,10,5,1,34,25,78]

l = len(mylist)
print "Length of the list is " + str(l)

m = max(mylist)
n = min(mylist)
print "Min n Max are " + str(m) + " " + str(n)

print list('tuhinkhareisthebestinthe world')

mylist[3] = 11
del mylist[3]


print "Adding into the middle of the 3rd position"
mylist[3:3] = [46,47,48]
print mylist

mylist2 = mylist;
mylist2[1:4] = []

print mylist2

mylist.append(34)
mylist.append(89)

print mylist


print mylist.count(89)
two = [90,91,92,93]
mylist.extend(two)
mylist.extend([6,7,8])

print mylist

print mylist.index(89)
num = mylist.pop(8)
print num

print mylist

mylist.insert(8,100)
print mylist

mylist.remove(89)
print mylist

mylist.reverse()
print mylist
