from selenium.webdriver.common.by import By

from FrameWorkWithDesign.utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shopLink = (By.CSS_SELECTOR, "a[href*='shop")
        self.productsCard = (By.XPATH, "//div[@class='card h-100']")
        self.checkOutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_product_to_cart(self, productName):
        self.driver.find_element(*self.shopLink).click()
        products = self.driver.find_elements(*self.productsCard)

        for product in products:
            productname = product.find_element(By.XPATH, "div/h4/a").text
            if productname == productName:
                product.find_element(By.XPATH, "div/button").click()

    def go_To_Cart(self):
        elementToClick = self.driver.find_elements(*self.checkOutBtn)[0]
        elementToClick.click()