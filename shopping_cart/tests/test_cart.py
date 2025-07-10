import pytest
import json
import os
from shopping_cart.cart import Cart
from shopping_cart.item import Item

@pytest.fixture
def test_database():
    """Create a temporary database file for testing."""
    db_path = "test_database.json"
    with open(db_path, "w") as f:
        json.dump({"Items": {}}, f)
    yield db_path
    # Clean up after the test
    if os.path.exists(db_path):
        os.remove(db_path)

def test_cart_creation(test_database):
    """Test that a cart can be created with the correct properties."""
    cart = Cart(test_database)
    assert cart.database_path == test_database
    assert cart.is_empty == True
    assert cart.is_active == False
    assert len(cart.id) == 6

def test_add_item_to_cart(test_database):
    """Test that an item can be added to the cart."""
    cart = Cart(test_database)
    item = Item("apple", "fruit", 1.25)
    cart.add_item_to_cart(item)
    
    # Check that the cart is no longer empty
    assert cart.is_empty == False
    assert cart.is_active == True
    
    # Check that the item was added to the database
    data = cart.get_all_items()
    assert len(data["Items"]) == 1
    assert data["Items"][item.id]["name"] == "apple"
    assert data["Items"][item.id]["type"] == "fruit"
    assert data["Items"][item.id]["price"] == 1.25

def test_get_total_price(test_database):
    """Test that the total price is calculated correctly."""
    cart = Cart(test_database)
    item1 = Item("apple", "fruit", 1.25)
    item2 = Item("banana", "fruit", 0.75)
    cart.add_item_to_cart(item1)
    cart.add_item_to_cart(item2)
    
    assert cart.get_total_price_of_items() == 2.0
