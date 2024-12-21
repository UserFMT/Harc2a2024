from selenium.webdriver.common.by import By

class mainPage:

    def __init__(self, driver, URL: str) -> None:
        self._driver = driver
        self._driver.get(URL)
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def buttons_click(self, name):
        buttons = self._driver.find_elements(By.CSS_SELECTOR, name)
        for button in buttons:
            button.click()

    def basket_count (self, name):
        dd = self._driver.find_element(By.ID, name).text
        return dd

    def add_basket(self, name):
        self.buttons_click(name)
        self._driver.implicitly_wait(20)
        self._driver.refresh()

    def delete_count_basket(self, name, selector, num):
        products = self.elements_class(name)
        i = 0
        while i < num:
             products[i].find_element(By.CSS_SELECTOR, selector).click()
             i+=1
        self._driver.implicitly_wait(20)

    def elements_class(self, name):
        return (self._driver.find_elements(By.CLASS_NAME,name))

    def elements_selector(self, name):
        return (self._driver.find_elements(By.CSS_SELECTOR, name))

    def element_path(self, name):
        return (self._driver.find_element(By.XPATH, name))

