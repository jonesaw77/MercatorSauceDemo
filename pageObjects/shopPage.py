from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    def add_highest_priced_item_to_cart(self):
        print("Adding highest priced item to cart...")

        # 1. Clear the cart
        self.driver.get("https://www.saucedemo.com/cart.html")
        for btn in self.driver.find_elements(By.CSS_SELECTOR, "button[class*='cart_button']"):
            btn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")

        # 2. Find and click the highest-priced item
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        highPrice = 0.0
        highPrice_item = None
        for item in items:
            price = float(item.find_element(By.CLASS_NAME, "inventory_item_price").text.replace("$", ""))
            if price > highPrice:
                highPrice = price
                highPrice_item = item

        assert highPrice_item, "No items found on inventory page"
        highPrice_item.find_element(By.CSS_SELECTOR, "button").click()

        # 3. Wait for the cart badge to show exactly "1"
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1")
        )
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 4. Verify only one item is in the cart
        basket_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        count = len(basket_items)
        assert count == 1, f"More than one item found in cart: {count} items"

        # 5. Read the price and return
        totalPrice = float(basket_items[0].text.replace("$", ""))
        print("DEBUG: Returning:", totalPrice, highPrice)
        return totalPrice, highPrice
