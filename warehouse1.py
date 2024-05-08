Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Warehouse:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.inventory = {}

...     def add_item(self, item, quantity):
...         if item in self.inventory:
...             self.inventory[item] += quantity
...         else:
...             self.inventory[item] = quantity
... 
...     def remove_item(self, item, quantity):
...         if item in self.inventory:
...             if self.inventory[item] >= quantity:
...                 self.inventory[item] -= quantity
...                 return True
...             else:
...                 return False
...         else:
...             return False
... 
...     def check_item_stock(self, item):
...         return self.inventory.get(item, 0)
... 
... # Example usage
... if __name__ == "__main__":
...     warehouse = Warehouse("Main Warehouse", 1000)
...     warehouse.add_item("Apples", 500)
...     warehouse.add_item("Bananas", 300)
... 
...     print("Current stock in Main Warehouse:")
...     for item, quantity in warehouse.inventory.items():
...         print(f"{item}: {quantity}")
... 
...     print("Checking stock of Apples:", warehouse.check_item_stock("Apples"))
...     print("Removing 200 Apples from stock...")
...     if warehouse.remove_item("Apples", 200):
...         print("200 Apples removed successfully.")
...     else:
...         print("Failed to remove 200 Apples, not enough stock.")
... 
...     print("Current stock in Main Warehouse after removal:")
...     for item, quantity in warehouse.inventory.items():
...         print(f"{item}: {quantity}")
