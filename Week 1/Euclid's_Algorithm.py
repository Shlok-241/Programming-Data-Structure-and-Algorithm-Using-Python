"""
Consider gcd(m,n) with m > n
If n diviides m return n
Otherwise, let r = m%n
Return gcd(m,n)
"""

def gcd(m,n):

    if m < n :
        (m,n) = (n,m)

    if (m%n) == 0:
        return n 

    else :
        return (gcd(n,m%n))


m = int(input("Enter a Number: "))
n = int(input("Enter another Number: "))

print(f"Greatest Common Divisor of {m} and {n} is {gcd(m,n)}")