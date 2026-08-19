# Consider the following lines of Python code.

b = [43,99,65,105,4]
a = b[2:]
d = b[1:]
c = b
d[1] = 95
b[2] = 47
c[3] = 73

"""


Which of the following holds at the end of this code?
(a) a[0] == 47, b[3] == 73, c[3] == 73, d[1] == 47
(b) a[0] == 65, b[3] == 105, c[3] == 73, d[1] == 95
(c) a[0] == 65, b[3] == 73, c[3] == 73, d[1] == 95
(d) a[0] == 95, b[3] == 73, c[3] == 73, d[1] == 95


"""