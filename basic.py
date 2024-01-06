from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from Logger import Logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger()

    def find_element(self, locator, time=10):
        try:
            obj = WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")
            self.logger.info(f"found {locator}")
            return obj
        except TimeoutException as error:
            self.logger.error(error)

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def wait_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(ec.invisibility_of_element_located(locator))

    def go_to_url(self):
        return self.driver.get(self.base_url)
