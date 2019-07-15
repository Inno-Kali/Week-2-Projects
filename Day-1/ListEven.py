#def even(x):
#    if x % 2 is 0:
##        print ("Even")
#         return True
#    
#    else:
##        print("Odd")
#         return False
#        
#        
#numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
#
#print(list(filter(even, numbers)))


#def even(x):
#    if x % 2 is 1:
##        print ("Even")
#         return True
#    
#    else:
##        print("Odd")
#         return False
        
        
#numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
#
#
#print([n for n in numbers if n%2==1])
#print([n for n in numbers if n%2==0])

List1=[x for x in range(1,51,1)]
print( List1)

List2 = [x for x in List1 if x % 2 == 1]

print("ODD Numbers : ",(List2))

List3 = [x for x in List1 if x % 2 == 0]

print("EVEN Numbers : ", List3)