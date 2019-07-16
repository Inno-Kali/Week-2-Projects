def is_even(x):
    if x % 2 is 0:
#        print ("Even")
         return True
    
    else:
#        print("Odd")
         return False
  
number = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]

sol = list(filter(is_even, number))
#print (list(lambda x: x % 2 is 0, number))
##sol = list(map(is_even, number))


print(sol)
#print(sol2)

def is_even(x):
    if x % 2 is 1:
#        print ("Even")
         return True
    
    else:
#        print("Odd")
         return False
  
number = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]

sol1 = list(filter(is_even, number))
#sol = list(map(is_even, number))


print(sol1)

#
#number = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
#
#print(list(lambda x : x % 2 == 0, number))