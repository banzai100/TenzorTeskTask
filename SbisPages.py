import os
import urllib.error
import urllib.request

from selenium.webdriver.common.by import By

from basic import BasePage


class SbisSearchHelper(BasePage):
    base_url = "https://sbis.ru/"
    LOCATORS = {"SBIS_CONTACTS": (By.CSS_SELECTOR, "[href='/contacts']"),
                "SBIS_TENSOR_BANNER": (By.CSS_SELECTOR, "[alt='Разработчик системы СБИС — компания «Тензор»']"),
                "SBIS_OVERLAY": (By.XPATH, "//div[@class='preload-overlay']"),
                "REGION_CHOOSER": (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']"),
                "PARTNERS_NAMES": (By.XPATH, "//div[contains(@class, 'sbisru-Contacts-List__name')]"),
                "KAMCHATKA_KRAI": (By.XPATH, "//span[@title='Камчатский край']"),
                "COOKIE_AGREEMENT_CLOSE": (By.XPATH, "//div[@class='sbis_ru-CookieAgreement__close']"),
                "DOWNLOAD_SBIS": (By.XPATH, "//a[contains(text(), 'Скачать СБИС')]"),
                "SBIS_PLUGIN": (By.XPATH,
                                "//div[contains(text(),'СБИС Плагин')]/following::div[@class='controls-tabButton__overlay']"),
                "SBIS_DOWNLOAD_WEB": (By.XPATH,
                                      "//h3[contains(text(),'Веб-установщик')]/following::a[@class='sbis_ru-DownloadNew-loadLink__link js-link']")
                }

    def click_button(self, button, wait=False, overlay="SBIS_OVERLAY"):
        if wait:
            self.wait_element(self.LOCATORS[overlay], time=5)
        return self.find_element(self.LOCATORS[button]).click()

    def download_web_installer(self):
        flag = False
        obj = self.find_element(self.LOCATORS["SBIS_DOWNLOAD_WEB"])
        url = obj.get_attribute("href")
        target = url.split("/")[-1]
        save_path = os.path.join(os.getcwd(), target)
        expected_size = float("".join([char for char in obj.text if char.isdigit() or char == "."]))
        try:
            urllib.request.urlretrieve(url, save_path)
        except urllib.error.URLError:
            self.logger.error("Web installer file not available")
            return flag
        if os.path.exists(save_path):
            file_size = round(os.path.getsize(save_path) / (1024 * 1024), 2)
            if file_size == expected_size:
                self.logger.info(f"Web installer file successfully download with size {file_size}")
                flag = True
            else:
                self.logger.error(f"Web installer file size incorrect")
        return flag
