#define the first function that computes the factorial operation
def factorial(y):
    fact = 1
    while y > 0:
        fact = fact * y
        y = y-1
    return fact
    
    
# Having defined the function above, call it each time with different arguments to fit the situation required. The simplified equation is n!/k!(n-k)!
def choose(n, k):
    result = factorial(n)/(factorial(k)*(factorial(n-k)))
    return result
