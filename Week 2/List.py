factors = [1, 2, 5, 10]
names = ["Anand", "Charles", "Muqsit"]
mixed = [3, True, "Yellow"] # A list containing an integer, a boolean, and a string

factors = [1, 2, 5, 10]
# factors[3] would be 10 (the element at index 3)
mixed = [3, True, "Yellow"]
# mixed[0:2] would be [3, True] (a sub-list from index 0 up to, but not including, index 2)
len(names) # returns 3

h = "hello"
# h[0] is "h"
# h[0:1] is "h"
# h[0] == h[0:1] is True

factors = [1, 2, 5, 10]
# factors[0] is 1 (an integer value)
# factors[0:1] is [1] (a list containing the integer 1)
# factors[0] == factors[0:1] is False (comparing an int to a list)

nested = [[2, [37]], 4, ["hello"]]
# nested[0] is [2, [37]] (the list at index 0)
# nested[1] is 4 (the integer at index 1)
# nested[2][0][3] is "l" (accessing the 3rd character of the 0th element of the list at index 2)
# nested[0][1:2] is [[37]] (a slice of the list at index 0, resulting in a list containing the list [37])

nested = [[2, [37]], 4, ["hello"]]
nested[1] = 7
# nested is now [[2, [37]], 7, ["hello"]]

nested = [[2, [37]], 7, ["hello"]] # Continuing from the previous example
nested[0][1][0] = 19
# nested is now [[2, [19]], 7, ["hello"]]


x = 5
y = x # y gets a copy of the value 5
x = 7 # x now refers to a new value 7; y remains 5


list1 = [1, 3, 5, 7]
list2 = list1 # list2 now refers to the *same* list object as list1
list1[2] = 4 # Modify the list object through list1
# list1 is now [1, 3, 4, 7]
# list2 is also [1, 3, 4, 7]


list1 = [1, 3, 5, 7]
list2 = list1[:] # list2 gets a *new* list object, a copy of list1's contents
list1[2] = 4 # Modify list1
# list1 is now [1, 3, 4, 7]
# list2 is still [1, 3, 5, 7]


list1 = [1, 3, 5, 7]
list2 = [1, 3, 5, 7]
list3 = list2

list1 == list2 # True (their contents are identical)
list2 == list3 # True (their contents are identical)

list1 = [1, 3, 5, 7]
list2 = [1, 3, 5, 7]
list3 = list2

list1 is list2 # False (they are two separate list objects, even if their values are the same)
list2 is list3 # True (list2 and list3 both refer to the *same* list object)


list1 = [1, 3, 5, 7]
list2 = [4, 5, 6, 8]
list3 = list1 + list2
# list3 is now [1, 3, 5, 7, 4, 5, 6, 8]


list1 = [1, 3, 5, 7]
list2 = list1 # list1 and list2 refer to the same object
list1 = list1 + [9] # This creates a *new* list and reassigns list1 to it
# list1 is now [1, 3, 5, 7, 9]
# list2 is still [1, 3, 5, 7]