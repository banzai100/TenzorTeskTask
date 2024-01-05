from SbisPages import SbisSearchHelper
from TenzorPages import TenzorSearchHelper


# import logging

# logging.basicConfig(level=logging.INFO, filename="test.log", encoding="utf-8", filemode="w")


def test_sbis_contacts(browser):
    sbis_main_page = SbisSearchHelper(browser)
    sbis_main_page.go_to_url()
    sbis_main_page.click_button("SBIS_CONTACTS")
    sbis_main_page.click_button("SBIS_TENSOR_BANNER", wait=True)
    sbis_main_page.driver.switch_to.window(sbis_main_page.driver.window_handles[1])
    tensor_main_page = TenzorSearchHelper(browser)
    tensor_main_page.find_element(tensor_main_page.LOCATORS["TENSOR_POWER_IN_PEOPLE"])
    tensor_main_page.click_button("TENSOR_ABOUT", wait=True)
    assert tensor_main_page.driver.current_url == "https://tensor.ru/about"
    tensor_main_page.find_element(tensor_main_page.LOCATORS["TENSOR_BLOCK3"])
    assert tensor_main_page.check_images("TENSOR_BLOCK3_IMAGES") == True
