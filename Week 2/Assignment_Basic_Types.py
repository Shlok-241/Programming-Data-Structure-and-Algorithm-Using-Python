# Interger type 
i = 5 
j = 2 * i 
j = j + 5 

# Float and arithmatic operators
a = 7 / 2 # Result: 3.5 (float)
b = 7 / 3.5 # Result: 2.0 (float)
c = 9 // 5 # Result: 1
d = 9 % 5 # Result: 4
e = 3 ** 4 # Result: 81 (3 * 3 * 3 * 3)

# Basic Transformation of Data type
i = 5 # 'i' is an int
i = 7 * 1 # 'i' is still an int (7 * 1 is 7)
j = i / 3 # 'j' becomes a float (7 / 3 is approx 2.33)
i = 2 * j # 'i' now becomes a float (2 * 2.33 is approx 4.66)

# Checking data type
type(i) # If i = 5, returns <class 'int'>
type(j) # If j = 2.33, returns <class 'float'>

# Boolean data type and use of (not,and,or)

a = not True # Result: False
b = not False # Result: True
c = True and True # Result: True
d = True and False # Result: False
e = True or False # Result: True
f = False or False # Result: False

# Check odd even
def divides(m, n):
    if n % m == 0:
        return(True)
    else:
        return(False)

def even(n):
    return(divides(2, n)) # Returns True if 2 divides n, False otherwise

def odd(n):
    return(not divides(2, n)) # Returns True if 2 does NOT divide n, False otherwise