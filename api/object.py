class Item:
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description

# for k,v in Item(1,2,3).__dict__.items():
#     print(k,v)
# library = {}
# for i in range(1,11):
#     item = Item(i,f'{i}-test',f'{i**2}').__dict__
#     library[str(i)] = item
#     print(library[str(i)])
