def fib_rec(n):
    if n == 1:
        return 1
    else:
        return n * fib_rec(n-1) -( n * n*fib_rec(n-2) )
    
print(fib_rec(4))