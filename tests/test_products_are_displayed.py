from pages.inventory_page import InventoryPage
import time

def test_products_are_displayed(setup_page):
    # Initialize the page object
    inventory_page = InventoryPage(setup_page)

    # Verify that products are displayed
    assert inventory_page.are_products_displayed(), "No products are displayed on the inventory page"
    

def test_product_details(inventory_page):
    expected_products = [
        {
            "name": "Sauce Labs Backpack",
            "description": "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
            "price": 29.99
        },
        {
            "name": "Sauce Labs Bike Light",
            "description": "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
            "price": 9.99
        },
        {
            "name": "Sauce Labs Bolt T-Shirt",
            "description": "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.",
            "price": 15.99
        },
        {
            "name": "Sauce Labs Fleece Jacket",
            "description": "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
            "price": 49.99
        },
        {
            "name": "Sauce Labs Onesie",
            "description": "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
            "price": 7.99
        },
        {
            "name": "Test.allTheThings() T-Shirt (Red)",
            "description": "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.",
            "price": 15.99
        }
    ]

    actual_products = inventory_page.get_product_details()

    for expected, actual in zip(expected_products, actual_products):
        assert expected["name"] == actual["name"], f"Expected name {expected['name']} but got {actual['name']}"
        assert expected["description"] == actual["description"], f"Expected description {expected['description']} but got {actual['description']}"
        assert expected["price"] == actual["price"], f"Expected price {expected['price']} but got {actual['price']}"

