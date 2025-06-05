class CartPage:
    def __init__(self, page):
        self.page = page

    def get_cart_total(self):
        # Locate and return the total price of items in the cart
        total_text = self.page.inner_text('.summary_subtotal_label')  # Adjust selector if needed
        # Extract the numerical value
        return float(total_text.split('$')[1])
