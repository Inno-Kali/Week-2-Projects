List1=[x for x in range(1,51,1)]
print( List1)

List2 = [x for x in List1 if x % 2 == 1]

print("ODD Numbers : ",(List2))

List3 = [x for x in List1 if x % 2 == 0]

print("EVEN Numbers : ", List3)