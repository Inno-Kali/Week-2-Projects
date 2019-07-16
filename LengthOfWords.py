words = ["hello", "my", "name", "is", "Sam"]

wd = [x.upper() for x in words]
print(wd)
print([len(word) for word in wd ])

print(tuple(zip(wd, [len(word) for word in wd ])))