def gcd(m,n):
    i = min(m,n)

    while i > 0:
        if (m%i) == 0 and (n%i) == 0:
            return (i)

    else:
        i -= 1

m = int(input("Enter a Number: "))
n = int(input("Enter another Number: "))

print(f"Greatest Common Divisor of {m} and {n} is {gcd(m,n)}")

"""

Instead of searching seprately we directly find common factor. 
We start the search from the minimum in (m,n) to 1 and the first factor is gcd

So the use of list is not required which saves our space and time both.

"""