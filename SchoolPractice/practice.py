class Item:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def description(self):
        return "[name: {}, color: {}, weight: {}]".format(self.name, self.color, self.weight)


#mitt_object = Item("Fish", "Red", "3kg")
#print(mitt_object.description())

class Bag:
    def __init__(self, label):
        self.label = label
        self.items = []

    def add_item(self, item_object):
        self.items = item_object

    def description(self):
        Item.description()
        return "{} contains the following:\n{}".format(self.label, Item.description(self.items))

bag = Bag("Min säck")
item_1 = Item("Fisk", "röd", 10.0)
item_2 = Item("Hund", "brun", 20.0)
item_3 = Item("Fredrik", "grön", 9001.0)
print(bag.description())