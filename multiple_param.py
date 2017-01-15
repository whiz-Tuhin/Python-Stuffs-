def mylist(*food):
    print food      # the parameter is treated as tuple


def myprofile(name,*companies):
    print "companies that [%s] has worked with are" % name
    print companies

def mydiet_profile(first,last,*ages,**items):
    print first,last
    print ages
    print items



mylist('apples','bananas','cheese','bread')

myprofile('tuhin','amazon','google','apple','cisco','zynga')

mydiet_profile('tuhin','khare',56,67,87,12,apples = 14,bananas = 3,meat = 5)
