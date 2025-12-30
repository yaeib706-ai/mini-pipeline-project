import pytest
from inventory import check_toy_inventory, add_toy_to_store

def test_check_toy_exists():
    inventory = ["Robot", "Doll", "Car"]
    assert check_toy_inventory("Robot", inventory) == True

def test_check_toy_missing():
    inventory = ["Robot", "Doll", "Car"]
    assert check_toy_inventory("Puzzle", inventory) == False

def test_add_new_toy():
    inventory = ["Robot"]
    updated_inventory = add_toy_to_store("Lego", inventory)
    assert "Lego" in updated_inventory
    assert len(updated_inventory) == 2