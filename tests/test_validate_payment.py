
def test_add_to_cart_and_validate_totals(inventory_page):
    # Step 3: Add products to the cart
    products = ['sauce-labs-backpack', 'sauce-labs-bike-light']
    for product in products:
        inventory_page.aadd_product_to_cart(product)

    # Step 4: Go to cart
    inventory_page.go_to_cart()

    # Step 5: Proceed to checkout
    inventory_page.proceed_to_checkout()

    # Step 6: Fill in checkout information
    inventory_page.fill_checkout_information("Michael", "Williams", "33445")

    # Step 7: Validate the total
    item_total = inventory_page.get_item_total()

    # Assuming the individual product prices are known
    expected_total = 29.99 + 9.99  # Replace with actual prices

    assert item_total == expected_total, f"Expected total {expected_total}, but got {item_total}"
