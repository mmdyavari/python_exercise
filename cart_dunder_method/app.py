import json

# get items from items.json
data = []
with open("cart_dunder_method/items.json", "r") as file:
    if file:
        file = json.load(file)
        for i in file:
            data.append([i["name"], i["price"]])


class Order:
    def __init__ (self, customer, *cart_items):
        self.customer = customer
        self.cart_items = []

        for i in list(cart_items):
            for data_item in data:
                if data_item[0] == i:
                    self.cart_items.append(i)
    
    # add new item in cart
    def __add__ (self, new_item):
        for i in data:
            if i[0] == new_item:
                self.cart_items.append(new_item)

    # remove an item in cart 
    def __sub__ (self, item):
        if item in self.cart_items:
            self.cart_items.remove(item)

    # get item with index
    def __getitem__ (self, index):
        return self.cart_items[index]
        
    # show cart
    def __call__ (self):
        return self.cart_items
    
    # return price of cart
    def price (self):
        su = 0 
        for i in self.cart_items:
            for data_item in data:
                if data_item[0] == i:
                    su += data_item[1]
        return su

    

if __name__ == "__main__":
    # user = Order("mohammad", "havij")

    # user + "havij"
    # user - "havij"
    # user + "khiar"

    # print(user[0])

    # print(user.price())

    # print(user())
    
    pass