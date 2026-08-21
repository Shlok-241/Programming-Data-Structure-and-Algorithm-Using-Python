list1 = [1, 3, 5, 6]
list2 = list1
list1[2] = 7
# list1 = [1,3,7,6]
# list2 = [1,3,7,6] because list1 = list2 both point at same list

list1 = [1, 3, 5, 6]
list2 = list1
list1 = list1 + [12] # Creates a new list for list1
# list1 is now [1, 3, 5, 6, 12]
# list2 remains [1, 3, 5, 6] because it still points to the original list



list1 = [1, 3, 5, 6]
list2 = list1
list1.append(12) # Modifies the list object in place
# list1 is now [1, 3, 5, 6, 12]
# list2 is also [1, 3, 5, 6, 12] because it points to the same modified object




list1 = [0, 1, 2]
list1.extend([13, 14]) # Extends list1 in place
# list1 is now [0, 1, 2, 13, 14]

list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2.remove(5) # Removes the first 5
# list2 is now [0, 1, 2, 3, 4, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
if x in l:
    l.remove(x) # Safely removes x if it exists

while x in l:
    l.remove(x) # Repeatedly removes x until no more are found



list1 = [1, 3, 5, 6]
list2 = list1
list1[2:] = [7, 8] # Replaces [5, 6] with [7, 8]
# Both list1 and list2 become [1, 3, 7, 8]

list1 = [1, 3, 7, 8]
list1[2:] = [9, 10, 11] # Replaces [7, 8] with [9, 10, 11]
# list1 becomes [1, 3, 9, 10, 11] (expanded from 4 to 5 elements)

list1 = [1, 3, 9, 10, 11]
list1[0:2] = [7] # Replaces [1, 3] with [7]
# list1 becomes [7, 9, 10, 11] (shrunk from 5 to 4 elements)


"""
def factors(n):
    If flist is not initialized here, Python won't know it's a list
    and flist.append(i) will cause an error.
    for i in range(1, n + 1):
        if n % i == 0:
            flist.append(i)  Error: flist is not defined or not a list
    return(flist)
"""    


def factors(n):
    flist = [] # Initialize flist as an empty list
    for i in range(1, n + 1):
        if n % i == 0:
            flist.append(i) # Now flist is known to be a list, append works
    return(flist)

