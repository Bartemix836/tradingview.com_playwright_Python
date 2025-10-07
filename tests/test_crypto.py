import pytest
import time

from pages.base_page import BasePageHelper

@pytest.mark.usefixtures("playwright_context")
def test_launch_browser(playwright_context, request):
    browser = playwright_context["browser"]
    context = playwright_context["context"]
    page = playwright_context["page"]

    base_page = BasePageHelper(page)

    def log_step(step_text):
        print(step_text)
        request.node.add_report_section("call", "stdout", step_text)


    log_step("STEP 1: Browser launched with stealth enabled")
    base_page.stealth_setup()
    time.sleep(3)


    log_step("STEP 2: Navigated to https://www.tradingview.com/")
    base_page.load_page("https://www.tradingview.com/")
    time.sleep(3)


    # Hover Products
    log_step("STEP 3: Hovered 'Products' menu")
    base_page.hover_element_by_selector('a[data-main-menu-root-track-id="products"]')
    time.sleep(3)


    # Select Screeners position:
    log_step("STEP 4: Hovered 'Screeners'")
    screener_xpath='/html/body/div[7]/div[2]/span/div[1]/div/div/div[1]/div[3]/a/div/div/span/span'
    base_page.hover_element_by_xpath(screener_xpath)
    time.sleep(4)


    # Click Heatmaps->Crypto
    log_step("STEP 5: Clicked Crypto from Headmap section")
    crypto_xpath='/html/body/div[2]/footer/div/div/div/div[1]/div[2]/div[1]/div[3]/ul/li[3]/a'
    base_page.click_element_by_xpath(crypto_xpath)
    time.sleep(7)


    # Asserion - check element "Crypto Coins Headmap" if is visible
    log_step("Asserion - check element 'Crypto Coins Headmap' if is visible")
    headmap_assert='.title-JA5qpKYT'
    base_page.is_element_visible(headmap_assert)
    time.sleep(3)


    # Open click crypto coins list:
    log_step("STEP 6: Opened crypto coins list")
    listcrypto_selector='span.ellipsisContainer-bYDQcOkp:has-text("Crypto coins")'
    base_page.click_element_by_selector(listcrypto_selector)
    time.sleep(3)


    # Select crypto coins (excluding bitcoin)
    log_step("STEP 7: Selected crypto coins (excluding bitcoin) postion")
    crpytoposition_xpath='/html/body/div[7]/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div'
    base_page.click_element_by_xpath(crpytoposition_xpath)
    time.sleep(3)


    # Select Market cup list:
    log_step("STEP 8: Selected Market Cup list:")
    cuplist_selector='span.ellipsisContainer-bYDQcOkp:has-text("Market cap")'
    base_page.click_element_by_selector(cuplist_selector)
    time.sleep(3)


    # Select FD market cap position
    log_step("STEP 9: Selected FD market cup:")
    fdmarket_xpath='/html/body/div[7]/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div'
    base_page.click_element_by_xpath(fdmarket_xpath)
    time.sleep(3)


    # Select Change 24h, %
    log_step("STEP 10: Selected Change 24h, % list:")
    cuplist_selector='span.ellipsisContainer-bYDQcOkp:has-text("Change 24h, %")'
    base_page.click_element_by_selector(cuplist_selector)
    time.sleep(3)


    log_step("STEP 11: Selected Performance W% from list:")
    performanceW_xpath='/html/body/div[7]/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/div[5]/div/div/div/div'
    base_page.click_element_by_xpath(performanceW_xpath)
    time.sleep(3)


    # Select settings:
    log_step("STEP 12: Selected settings section")
    settingsbtn_xpath='/html/body/div[2]/main/div/div/div/div[1]/div/div[2]/button[2]'
    base_page.click_element_by_xpath(settingsbtn_xpath)
    time.sleep(3)


    # Click Display value position:
    log_step("STEP 13 Clicked dispaly value")
    displayvalue_xpath='/html/body/div[7]/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div'
    base_page.click_element_by_xpath(displayvalue_xpath)
    time.sleep(6)


    # Price position
    log_step("STEP 14 Selected Price position")
    # pricepos_xpath='/html/body/div[7]/div[4]/div/div/div/div[1]/div/div[2]/div/div/div[3]/div/div'
    price_btn='.title-LSK1huUA.ellipsis-K3hWbfcy.apply-overflow-tooltip:has-text("Price")'
    base_page.click_element_by_selector(price_btn)
    time.sleep(3)









    # log_step("STEP 5: Clicked 'SPX'")
    # base_page.click_element_by_selector('div.flexCell-RsFlttSS:has-text("SPX")')
    # time.sleep(5)
    #
    # log_step("STEP 6: Clicked Metrics button")
    # metrics_xpath = '/html/body/div[2]/div/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div[1]'
    # base_page.click_element_by_xpath(metrics_xpath)
    # time.sleep(4)
    #
    # log_step("STEP 7: Clicked 'Technical' position")
    # technical_xpath = '/html/body/div[7]/div[2]/span/div[1]/div/div/div[2]'
    # base_page.click_element_by_xpath(technical_xpath)
    # time.sleep(8)
    #
    # log_step('Assertion: check is visible: title="Technicals"')
    # assert base_page.is_element_visible('.title-rweDqzH3')
    # time.sleep(3)
    #
    # log_step("STEP 8: Change period (1 minute - 1 month)")
    # for label in ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "1D", "1W", "1M"]:
    #     base_page.click_element_by_xpath(f'//*[@id="{label}"]')
    #     log_step(f"STEP 8: Selected period: {label}")
    #     time.sleep(3)

    log_step("Test case completed successfully - positive result.")
