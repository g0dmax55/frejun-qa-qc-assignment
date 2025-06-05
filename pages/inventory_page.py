from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_dropdown_selector = ".product_sort_container"
        self.item_name_selector = ".inventory_item_name"
        self.item_price_selector = ".inventory_item_price"
        self.item_desc_selector = ".inventory_item_desc"  # Ensure this is defined
        self.inventory_item_selector = ".inventory_item"

    def sort_products(self, sort_option: str):
        """Select a sort option from the dropdown."""
        self.page.select_option(self.sort_dropdown_selector, sort_option)

    def get_item_names(self):
        """Retrieve all item names from the page."""
        return self.page.locator(self.item_name_selector).all_text_contents()

    def get_item_prices(self):
        """Retrieve all item prices from the page and convert them to floats."""
        price_texts = self.page.locator(self.item_price_selector).all_text_contents()
        return [float(price.replace("$", "")) for price in price_texts]

    def are_products_displayed(self):
        """Check if any products are displayed on the page."""
        return self.page.locator(self.inventory_item_selector).count() > 0

    def get_product_details(self):
        """Retrieve all product details as a list of dictionaries."""
        items = self.page.query_selector_all(self.inventory_item_selector)  # Corrected to use inventory_item_selector
        product_details = []
        for item in items:
            name = item.query_selector(self.item_name_selector).inner_text()
            desc = item.query_selector(self.item_desc_selector).inner_text()
            price_text = item.query_selector(self.item_price_selector).inner_text()
            price = float(price_text.replace("$", ""))
            product_details.append({
                "name": name,
                "description": desc,
                "price": price
            })
        return product_details

    def login(self, username, password):
        self.page.fill('data-test=username', username)
        self.page.fill('data-test=password', password)
        self.page.click('data-test=login-button')

    def aadd_product_to_cart(self, product_name):
        # Construct the button selector using the product name
        specific_button_selector = f"button[data-test='add-to-cart-{product_name}']"
        
        # Attempt to click the button directly using the specific button selector
        try:
            self.page.click(specific_button_selector)
        except Exception as e:
            print(f"Direct click on {specific_button_selector} failed: {e}")
            # Fallback to locating the product container and then the button
            product_container_selector = f".inventory_item:has-text('{product_name}')"
            add_to_cart_button_selector = f"{product_container_selector} button[data-test='add-to-cart']"
            self.page.click(add_to_cart_button_selector)



    def go_to_cart(self):
        self.page.click("[data-test='shopping-cart-link']")

    def proceed_to_checkout(self):
        self.page.click("[data-test='checkout']")

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.page.fill("[data-test='firstName']", first_name)
        self.page.fill("[data-test='lastName']", last_name)
        self.page.fill("[data-test='postalCode']", postal_code)
        self.page.click("[data-test='continue']")

    def get_item_total(self):
        item_total_text = self.page.inner_text(".summary_subtotal_label")
        return float(item_total_text.split('$')[1])

    def add_product_to_cart(self, product_name):
        # Click on the product based on its name to ensure the correct context
        self.page.click(f"text={product_name}")

        # Click the "Add to cart" button
        self.page.click('button[data-test="add-to-cart"]')


    def go_to_cart(self):
        self.page.click('.shopping_cart_link')