def fib(n):
    # from http://en.literateprograms.org/Fibonacci_numbers_(Python)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
if __name__ == '__main__':
    import sys
    
    n = int(sys.argv[1])
    resultat = fib(n)
    print resultat