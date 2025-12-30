def check_toy_inventory(toy_name, inventory_list):
    """
    פונקציה הבודקת אם צעצוע קיים ברשימת המלאי.
    """
    if toy_name in inventory_list:
        return True
    return False

def add_toy_to_store(toy_name, inventory_list):
    """
    מוסיפה צעצוע חדש למלאי ומחזירה את הרשימה המעודכנת.
    """
    if toy_name not in inventory_list:
        inventory_list.append(toy_name)
    return inventory_list