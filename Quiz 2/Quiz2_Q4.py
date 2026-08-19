#What is the value of mylist after the following lines are executed?

def mystery(l):
    l = l[2:]
    return(l)

mylist = [7,11,13,17,19,21]
mystery(mylist)