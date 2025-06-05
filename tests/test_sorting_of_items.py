from pages.inventory_page import InventoryPage

def test_sort_by_name_az(setup_page):
    inventory_page = InventoryPage(setup_page)
    inventory_page.sort_products("az")
    
    item_names = inventory_page.get_item_names()
    sorted_names = sorted(item_names)
    assert item_names == sorted_names, "Items are not sorted by name A-Z"

def test_sort_by_name_za(setup_page):
    inventory_page = InventoryPage(setup_page)
    inventory_page.sort_products("za")
    
    item_names = inventory_page.get_item_names()
    sorted_names = sorted(item_names, reverse=True)
    assert item_names == sorted_names, "Items are not sorted by name Z-A"

def test_sort_by_price_lohi(setup_page):
    inventory_page = InventoryPage(setup_page)
    inventory_page.sort_products("lohi")
    
    item_prices = inventory_page.get_item_prices()
    sorted_prices = sorted(item_prices)
    assert item_prices == sorted_prices, "Items are not sorted by price low to high"

def test_sort_by_price_hilo(setup_page):
    inventory_page = InventoryPage(setup_page)
    inventory_page.sort_products("hilo")
    
    item_prices = inventory_page.get_item_prices()
    sorted_prices = sorted(item_prices, reverse=True)
    assert item_prices == sorted_prices, "Items are not sorted by price high to low"
