from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout_with_backpack(setup_page):
    inventory_page = InventoryPage(setup_page)
    inventory_page.add_product_to_cart('Sauce Labs Backpack')
    inventory_page.go_to_cart()
    setup_page.click('button[data-test="checkout"]')

    checkout_page = CheckoutPage(setup_page)
    checkout_page.enter_shipping_information("John", "Doe", "12345")
    checkout_page.continue_to_overview()

    assert "Thank you for your order!" in checkout_page.get_confirmation_message()

def test_complete_checkout_with_bike_light(setup_page):
    inventory_page = InventoryPage(setup_page)
    inventory_page.add_product_to_cart('Sauce Labs Bike Light')
    inventory_page.go_to_cart()
    setup_page.click('button[data-test="checkout"]')

    checkout_page = CheckoutPage(setup_page)
    checkout_page.enter_shipping_information("Jane", "Smith", "67890")
    checkout_page.continue_to_overview()

    assert "Thank you for your order!" in checkout_page.get_confirmation_message()

def test_complete_checkout_with_bolt_tshirt(setup_page):
    inventory_page = InventoryPage(setup_page)
    inventory_page.add_product_to_cart('Sauce Labs Bolt T-Shirt')
    inventory_page.go_to_cart()
    setup_page.click('button[data-test="checkout"]')

    checkout_page = CheckoutPage(setup_page)
    checkout_page.enter_shipping_information("Alice", "Johnson", "11223")
    checkout_page.continue_to_overview()

    assert "Thank you for your order!" in checkout_page.get_confirmation_message()

def test_complete_checkout_with_fleece_jacket(setup_page):
    inventory_page = InventoryPage(setup_page)
    inventory_page.add_product_to_cart('Sauce Labs Fleece Jacket')
    inventory_page.go_to_cart()
    setup_page.click('button[data-test="checkout"]')

    checkout_page = CheckoutPage(setup_page)
    checkout_page.enter_shipping_information("Michael", "Williams", "33445")
    checkout_page.continue_to_overview()

    assert "Thank you for your order!" in checkout_page.get_confirmation_message()

def test_complete_checkout_with_onesie(setup_page):
    inventory_page = InventoryPage(setup_page)
    inventory_page.add_product_to_cart('Sauce Labs Onesie')
    inventory_page.go_to_cart()
    setup_page.click('button[data-test="checkout"]')

    checkout_page = CheckoutPage(setup_page)
    checkout_page.enter_shipping_information("Emily", "Brown", "55667")
    checkout_page.continue_to_overview()

    assert "Thank you for your order!" in checkout_page.get_confirmation_message()

def test_complete_checkout_with_testallthethings_tshirt(setup_page):
    inventory_page = InventoryPage(setup_page)
    inventory_page.add_product_to_cart('Test.allTheThings() T-Shirt (Red)')
    inventory_page.go_to_cart()
    setup_page.click('button[data-test="checkout"]')

    checkout_page = CheckoutPage(setup_page)
    checkout_page.enter_shipping_information("David", "Garcia", "77889")
    checkout_page.continue_to_overview()

    assert "Thank you for your order!" in checkout_page.get_confirmation_message()



def test_checkout_with_minimum_information(setup_page):
    inventory_page = InventoryPage(setup_page)
    inventory_page.add_product_to_cart('Sauce Labs Backpack')
    inventory_page.go_to_cart()
    setup_page.click('button[data-test="checkout"]')

    checkout_page = CheckoutPage(setup_page)
    # Enter only first name and postal code, leave last name empty
    checkout_page.enter_shipping_information("John", "", "12345")

    # Check for specific error message about missing last name
    error_message = setup_page.query_selector('[data-test="error"]').inner_text()
    assert "Error: Last Name is required" in error_message, "Expected error message about last name not displayed"


def test_checkout_with_empty_cart_allows_navigation(setup_page):
    inventory_page = InventoryPage(setup_page)
    # Navigate directly to the cart without adding any products
    inventory_page.go_to_cart()
    
    # Click the checkout button
    setup_page.click('button[data-test="checkout"]')
    
    # Verify that the checkout page is displayed even with an empty cart
    checkout_page = CheckoutPage(setup_page)
    assert checkout_page.is_displayed(), "Checkout page should be displayed even with an empty cart"
