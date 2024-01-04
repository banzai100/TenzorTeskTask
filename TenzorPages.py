from basic import BasePage
from selenium.webdriver.common.by import By


class TenzorSearchLocators:
    LOCATOR_TENZOR_POWER_IN_PEOPLE = (By.XPATH, "//p[contains(text(),'Сила в людях')]")


class TenzorSearchHelper(BasePage):
    def find_element_power(self):
        return self.find_element(TenzorSearchLocators.LOCATOR_TENZOR_POWER_IN_PEOPLE, time=2)

