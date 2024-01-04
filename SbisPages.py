from basic import BasePage
from selenium.webdriver.common.by import By


class SbisSearchLocators:
    LOCATOR_SBIS_CONTACTS = (By.CSS_SELECTOR, "[href='/contacts']")
    LOCATOR_SBIS_TENZOR = (By.CSS_SELECTOR, "[alt='Разработчик системы СБИС — компания «Тензор»']")
    LOCATOR_SBIS_TENZOR_OVERLAY = (By.XPATH, "//div[@class='preload-overlay']")



class SbisSearchHelper(BasePage):
    def click_contact_button(self):
        return self.find_element(SbisSearchLocators.LOCATOR_SBIS_CONTACTS, time=2).click()

    def click_tenzor_button(self):
        self.wait_element(SbisSearchLocators.LOCATOR_SBIS_TENZOR_OVERLAY, time=2)
        return self.find_element(SbisSearchLocators.LOCATOR_SBIS_TENZOR, time=2).click()


