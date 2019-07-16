#def factorial(n):
#    x = 1
#   
#    while n > 1:
#       
#        x = x * n
#        n = n-1
#        print(x)
#        
#        
#factorial(4)

#Alternative

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(11))