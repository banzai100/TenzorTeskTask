from SbisPages import SbisSearchHelper
from TenzorPages import TenzorSearchHelper
from time import sleep


def test_sbis_contacts(browser):
    sbis_main_page = SbisSearchHelper(browser)
    sbis_main_page.go_to_url()
    sbis_main_page.click_contact_button()
    sbis_main_page.click_tenzor_button()
    sbis_main_page.driver.switch_to.window(sbis_main_page.driver.window_handles[1])
    tenzor_main_page = TenzorSearchHelper(browser)
    tenzor_main_page.find_element_power()
    sleep(5)

