import pytest
from shopping_cart.item import Item

def test_item_creation():
    """Test that an item can be created with the correct properties."""
    item = Item("apple", "fruit", 1.25)
    assert item.name == "apple"
    assert item.type == "fruit"
    assert item.price == 1.25
    assert len(item.id) == 6

def test_item_price_rounding():
    """Test that the price is rounded to 2 decimal places."""
    item = Item("banana", "fruit", 0.567)
    assert item.price == 0.57

def test_item_search_string():
    """Test that the search string is correctly formatted."""
    item = Item("carrot", "vegetable", 0.75)
    assert item.search_string == "carrot vegetable"

def test_item_price()->None:
    item = Item("Car","vehicle",1200.02)
    assert item.price >= 0.0 or item.price == 1200.02

def test_item_name()->None:
    item = Item("a","b", 16.00)
    assert len(item.name)>0
