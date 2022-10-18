# variables
var = True
var = False

print(False + 5)
print(True + 5.5)

items = [1,2,3,4,5,'x',False,None]
items[-1] = 100
items.pop(0)
items.append(1)
items.insert(2,'test')
print(items[0],items[-1])
print(items)

items = (1,2,3,4)
print(items[0],items[-1])

print(len(items))

for i in items:
    print(i)
