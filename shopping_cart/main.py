from shopping_cart.item import Item
from shopping_cart.cart import Cart

if __name__ == "__main__":
    # the main database for the cart to pass to the class
    database = "./database.json"
    my_cart = Cart(database)

    #search for an item
    print("Searching Item...")
    result = my_cart.search_items("apple")
    print("---------------------------------------")

    #get the total amount of items in the cart
    print("Total items in the current cart:")
    total_item_count = my_cart.get_total_items_count()
    print(f"Total items: {total_item_count}")

    print("----------------------------------------")

    #Create an item object so it can be added to the cart
    print("Adding items to the cart...")
    print("----------------------------------------")
    milk = Item("milk","liquid",1.23)
    my_cart.add_item_to_cart(milk)
    onion = Item("onion","vegetable",0.43)
    my_cart.add_item_to_cart(onion)

    # Get all the items in the cart
    print("----------------------------------------")
    print("Getting all the items in the cart:")
    print("----------------------------------------")
    my_cart.get_all_items(verbose=1)

    print("----------------------------------------")

    #remove all the items by name or type
    print("Removing items from the cart...")
    print("---------------------------------------")
    my_cart.remove_item_by_query("milk")
    print("\n")
    # Remove a selected item
    print("Removing a specific item from the cart...")
    print("----------------------------------------")
    my_cart.remote_items_from_cart_by_selection()
    print("----------------------------------------")

    print("All the current items in the cart:")
    my_cart.get_all_items(verbose=1)
    print("----------------------------------------")

    print("Total price for all the items in the cart:")
    total_price = my_cart.get_total_price_of_items()
    print(f"{total_price}")
