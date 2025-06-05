class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def enter_shipping_information(self, first_name, last_name, postal_code):
        self.page.fill('input[data-test="firstName"]', first_name)
        self.page.fill('input[data-test="lastName"]', last_name)
        self.page.fill('input[data-test="postalCode"]', postal_code)
        self.page.click('input[data-test="continue"]')

    def continue_to_overview(self):
        # Assuming the continue button is after entering shipping details
        self.page.click('button[data-test="finish"]')


    def get_confirmation_message(self):
        return self.page.text_content('.complete-header')  


    def is_displayed(self):
        # Check if the element is visible using the corrected locator format
        return self.page.is_visible('[data-test="continue"]')
