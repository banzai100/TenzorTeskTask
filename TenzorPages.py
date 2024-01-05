from basic import BasePage
from selenium.webdriver.common.by import By


class TenzorSearchHelper(BasePage):
    base_url = "https://tensor.ru/"
    LOCATORS = {"TENSOR_POWER_IN_PEOPLE": (By.XPATH, "//p[contains(text(),'Сила в людях')]"),
                "TENSOR_ABOUT": (By.XPATH, "//a[@href='/about']"),
                "TENSOR_OVERLAY": (By.XPATH, "//div[@class='preload-overlay']"),
                "TENSOR_BLOCK3": (By.XPATH, "//div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__block3']"),
                "TENSOR_BLOCK3_IMAGES": (By.XPATH, "//div[contains(@class, 'tensor_ru-About__block3')]/descendant::img")
                }

    def click_button(self, button, wait=False):
        if wait:
            self.wait_element(self.LOCATORS["TENSOR_OVERLAY"], time=5)
        return self.find_element(self.LOCATORS[button], time=2).click()

    def check_images(self, locator):
        images = self.find_elements(self.LOCATORS[locator])
        return all([img.get_attribute("width") == images[0].get_attribute("width") for img in images]) and \
                all([img.get_attribute("height") == images[0].get_attribute("height") for img in images])
