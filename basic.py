from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Отсутствует элемент {locator}")

    def wait_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(ec.invisibility_of_element_located(locator))

    def go_to_url(self):
        return self.driver.get(self.base_url)
