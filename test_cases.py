from SbisPages import SbisSearchHelper
from TensorPages import TensorSearchHelper
from time import sleep


def test_case1(browser):
    sbis_main_page = SbisSearchHelper(browser)
    sbis_main_page.go_to_url()
    sbis_main_page.click_button("SBIS_CONTACTS")
    sbis_main_page.click_button("SBIS_TENSOR_BANNER", wait=True)
    sbis_main_page.driver.switch_to.window(sbis_main_page.driver.window_handles[1])
    tensor_main_page = TensorSearchHelper(browser)
    assert tensor_main_page.find_element(
        tensor_main_page.LOCATORS["TENSOR_POWER_IN_PEOPLE"]), "Power in people block not found"
    tensor_main_page.click_button("TENSOR_ABOUT", wait=True)
    assert tensor_main_page.driver.current_url == "https://tensor.ru/about", "Incorrect current url"
    tensor_main_page.find_element(tensor_main_page.LOCATORS["TENSOR_BLOCK3"])
    assert tensor_main_page.check_images("TENSOR_BLOCK3_IMAGES"), "Images have different dimensions"


def test_case2(browser):
    sbis_main_page = SbisSearchHelper(browser)
    sbis_main_page.go_to_url()
    sbis_main_page.click_button("SBIS_CONTACTS", wait=True)
    assert sbis_main_page.find_element(sbis_main_page.LOCATORS["REGION_CHOOSER"]).text == "Свердловская обл." and \
           sbis_main_page.find_element(sbis_main_page.LOCATORS["PARTNERS_LIST"]).text == "Екатеринбург", \
        "Wrong region or no partners list"

    sbis_main_page.click_button("REGION_CHOOSER", wait=True)
    sbis_main_page.click_button("KAMCHATKA_KRAI", wait=True)

    assert sbis_main_page.find_element(sbis_main_page.LOCATORS["REGION_CHOOSER"]).text == "Камчатский край" and \
           sbis_main_page.find_element(sbis_main_page.LOCATORS["PARTNERS_LIST"]).text == "Петропавловск-Камчатский", \
        "Wrong region or no partners list"
    assert sbis_main_page.driver.current_url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients", \
        "Incorrect current url"


def test_case3(browser):
    sbis_main_page = SbisSearchHelper(browser)
    sbis_main_page.go_to_url()
    sbis_main_page.click_button("COOKIE_AGREEMENT_CLOSE")
    sbis_main_page.click_button("DOWNLOAD_SBIS")
    sleep(1.5)
    sbis_main_page.click_button("SBIS_PLUGIN")
    assert sbis_main_page.download_web_installer(), "File not available or size incorrect"
