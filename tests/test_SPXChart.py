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

    log_step("STEP 3: Hovered 'Products' menu")
    base_page.hover_element_by_selector('a[data-main-menu-root-track-id="products"]')
    time.sleep(3)

    log_step("STEP 4: Clicked 'Supercharts'")
    base_page.click_element_by_selector('a[class="menuItem-bWyNMkwZ active-bWyNMkwZ"]')
    time.sleep(4)

    log_step("STEP 5: Clicked 'SPX'")
    base_page.click_element_by_selector('div.flexCell-RsFlttSS:has-text("SPX")')
    time.sleep(5)

    log_step("STEP 6: Clicked Metrics button")
    metrics_xpath = '/html/body/div[2]/div/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div[1]'
    base_page.click_element_by_xpath(metrics_xpath)
    time.sleep(4)

    log_step("STEP 7: Clicked 'Technical' position")
    technical_xpath = '/html/body/div[7]/div[2]/span/div[1]/div/div/div[2]'
    base_page.click_element_by_xpath(technical_xpath)
    time.sleep(8)

    log_step('Assertion: check is visible: title="Technicals"')
    assert base_page.is_element_visible('.title-rweDqzH3')
    time.sleep(3)

    log_step("STEP 8: Change period (1 minute - 1 month)")
    for label in ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "1D", "1W", "1M"]:
        base_page.click_element_by_xpath(f'//*[@id="{label}"]')
        log_step(f"STEP 8: Selected period: {label}")
        time.sleep(3)

    log_step("Test case completed successfully - positive result.")
