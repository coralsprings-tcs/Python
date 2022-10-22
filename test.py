items = [1,2,3,4,5]
# for item in items:
#     print(item)

# index = 0
# while True:
#     if index >= len(items):
#         break
#     print(items[index])
#     index += 1

index = 0
while index < len(items):
    print(items[index])
    index += 1

while True:
    try:
        print(items[index])
    except Exception as e:
        print(f'{e} - index was {index}')
        break
    index += 1

try:
    print(5+'a string')
except TypeError:
    print('tried matching different things')