friends = ['jaishree','ayush','kaustubh','harshil','kritik','shubhang']


print friends[3]
print friends[-4]

string = "tuhin"

print string[2]


#### Slicing Lists ####

print friends[2:5]

list = [1,2,3,4,5,6,7,8,9,10]

print list[0:10]

print list[1:3]
print list[2:4]

#backwards

#the second index is exclusive remember

print "Now we'll extract backwards"

print list[-5:-10:-1]
print list[-10:-3]

print list[:]
print list[::2]
print list[::-2]

print list[9:0:-2]

# Editing Sequences




#Sllicing lists

mylist = list('jaishreedhage')
mylist[8:] = list('khare')

print mylist
