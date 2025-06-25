import json
from dataclasses import dataclass, field

from shopping_cart.file_io import Fstream
from shopping_cart.random_number_utils import RandomUtils
from shopping_cart.item import Item


@dataclass
class Cart:
    database_path: str
    is_empty: bool = True
    is_active: bool = False
    id: str = field(init=False, default=RandomUtils.generate_random_id())

    def get_all_items(self, verbose=0)->dict:
        """
        Reads and returns a hash map with all the available items
        Args:
            if verbose is set 1, it will print all the items.
        Returns:
            dict: a hash map with all the items in the database
        """
        data_file = Fstream.load_json_files(self.database_path)
        if len(data_file.items()) > 0:
            self.is_empty = False
            self.is_active = True

        try:
            if verbose == 1:
                Fstream.print_json_structure(data_file)
                return data_file
            else:
                return data_file
        except:
            raise ValueError("The value for the verbose as to be 0 or 1")

    def search_items(self,query:str)->list[Item]:
        """
        Searches items in the database
        Args:
            query: search query
        Returns:
            list[Item]: a list of Item
        """
        data = Fstream.load_json_files(self.database_path)
        matching_items = []
        for item_id, item_data in data["Items"].items():
            item = Item(name=item_data["name"], type=item_data["type"],_price=item_data["price"],id=item_id)
            if query.lower() in item.search_string.lower():
                matching_items.append(item)

        if len(matching_items) == 0:
            print("No matching items found")
        else:
            for item in matching_items:
                print(f"Found: {item.name} {item.type} ${item.price}")

        return matching_items

    def get_total_items_count(self)->int:
        """
        Returns the total number of items in the cart.

        Returns:
            int: the total number of items in the cart
        """
        data = self.get_all_items()
        return len(data["Items"].items())

    def add_item_to_cart(self,item:Item):
        """
        Adds an item to the cart and update the database json file.

        Args:
            item (Item): the item to add to the cart
        """

        data = self.get_all_items()

        new_item = {
            "name": item.name,
            "type": item.type,
            "price": item.price,
        }

        data["Items"][item.id] = new_item

        with open(self.database_path,"w") as file:
            json.dump(data, file,indent=4)

        self.is_empty = False
        self.is_active = True

        print(f"Added {item.name} {item.type} ${item.price}")

    def remove_item_by_query(self,query:str)->None:
        """
        Removes all the instance of an item from the cart based on the query.

        Args:
            query (str): the query to find the item to remove.
        """

        data = self.get_all_items()
        items_to_remove = []

        for item_id, item_data in data["Items"].items():
            if query.lower() in item_data["name"].lower() or query.lower() in item_data["type"].lower():
                items_to_remove.append(item_id)

        if not items_to_remove:
            print(f"No matching items found: '{query}'")
            return

        for item_id in items_to_remove:
            item_name = data["Items"][item_id]["name"]
            del data["Items"][item_id]
            print(f"Removed: {item_name} from the cart.")

        with open(self.database_path,"w") as file:
            json.dump(data, file,indent=4)

        if not data["Items"]:
            self.is_empty = True
            self.is_active = False

    def remote_items_from_cart_by_selection(self):
        """
        Removes the selected item by index
        """
        data = self.get_all_items()
        items = []
        i = 1
        for item_id, item_data in data["Items"].items():
            items.append(item_id)
            print(f"{i}:{item_data}")
            i += 1

        try:
            usr_choice = int(input("Select the item to delete by number, example:0: ")) - 1
        except:
            raise ValueError("You must select a valid number!")

        item_to_delete = items[usr_choice]
        item_name = data["Items"][item_to_delete]["name"]
        del data["Items"][item_to_delete]
        print(f"Removed {item_name} from the cart.")

        with open(self.database_path,"w") as file:
            json.dump(data, file,indent=4)

        if not data["Items"]:
            self.is_empty = True
            self.is_active = False

    def get_total_price_of_items(self)->float:
        """
        Returns the total price of the items in the cart.
        """
        data = self.get_all_items()
        total_amount = 0
        for item_id, item_data in data["Items"].items():
            total_amount += item_data["price"]

        return total_amount

    def empty_cart(self):
        """
        Clear all the items in the cart.
        """
        data = self.get_all_items()
        if len(data["Items"].items()) > 0:
            data = {"Items": {}}
            with open(self.database_path,"w") as file:
                json.dump(data, file,indent=4)
            if not data["Items"]:
                self.is_empty = True
                self.is_active = False
            print("The cart is empty.")
        else:
            print("The cart is already empty.")
