# Fibonachi implementation using memoization.

def memoize(f):
    mem={}

    def memoized_function(n):
        if n not in mem:
            mem[n]=f(n)
        return mem[n]
    return memoized_function

# @ is a decorator, used as syntactic sugar for higher order functions.
# @memoize is equivalent to fib=memoize(fib)
 
@memoize
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-2) + fib(n-1)





fib=memoize(fib)

print(fib(2))

