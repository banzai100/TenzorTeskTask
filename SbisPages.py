from basic import BasePage
from selenium.webdriver.common.by import By


class SbisSearchHelper(BasePage):
    base_url = "https://sbis.ru/"
    LOCATORS = {"SBIS_CONTACTS": (By.CSS_SELECTOR, "[href='/contacts']"),
                "SBIS_TENSOR_BANNER": (By.CSS_SELECTOR, "[alt='Разработчик системы СБИС — компания «Тензор»']"),
                "SBIS_OVERLAY": (By.XPATH, "//div[@class='preload-overlay']"),
                "REGION_CHOOSER": (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']"),
                "PARTNERS_LIST": (By.XPATH, "//div[@id='city-id-2']"),
                "KAMCHATKA_KRAI": (By.XPATH, "//span[@title='Камчатский край']")
                }

    def click_button(self, button, wait=False):
        if wait:
            self.wait_element(self.LOCATORS["SBIS_OVERLAY"], time=5)
        return self.find_element(self.LOCATORS[button], time=2).click()

