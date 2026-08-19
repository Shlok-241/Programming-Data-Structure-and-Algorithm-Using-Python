# Basic Function

def power(x,n):
    ans = 1
    for i in range(0,n):
        ans = ans*x
    return(ans)


def update(l,i,v):
    if i >= 0 and i < len(l):
        l[i] = v
        return(True)
    else:
        v = v+1 # This line is for illustration of immutable behavior
    return(False)


# Recursive Function

def factorial(n):
    if n <= 0: # Base case: stops the recursion
        return(1)
    else: # Recursive step: calls itself with a smaller problem
        val = n * factorial(n-1)
    return(val)

