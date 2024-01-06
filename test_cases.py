from SbisPages import SbisSearchHelper
from TensorPages import TensorSearchHelper
import logging

logging.basicConfig(level=logging.INFO, filename="test.log", encoding="utf-8", filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')


def test_case1(browser):
    sbis_main_page = SbisSearchHelper(browser)
    sbis_main_page.go_to_url()
    sbis_main_page.click_button("SBIS_CONTACTS")
    sbis_main_page.click_button("SBIS_TENSOR_BANNER", wait=True)
    sbis_main_page.driver.switch_to.window(sbis_main_page.driver.window_handles[1])
    tensor_main_page = TensorSearchHelper(browser)
    assert bool(tensor_main_page.find_element(tensor_main_page.LOCATORS["TENSOR_POWER_IN_PEOPLE"])), "Power in people block not found"
    tensor_main_page.click_button("TENSOR_ABOUT", wait=True)
    assert tensor_main_page.driver.current_url == "https://tensor.ru/about", "Incorrect current url"
    tensor_main_page.find_element(tensor_main_page.LOCATORS["TENSOR_BLOCK3"])
    assert tensor_main_page.check_images("TENSOR_BLOCK3_IMAGES") == True, "Images have different dimensions"
