from playwright.sync_api import Page
import time
import random

class BasePageHelper:  # <-- zmiana nazwy z TestHelper
    def __init__(self, page: Page):
        self.page = page

    # --------------------------
    # Podstawowe opóźnienia
    # --------------------------
    def _human_delay(self, min_delay=0.3, max_delay=1.0):
        time.sleep(random.uniform(min_delay, max_delay))

    # --------------------------
    # Stealth / maskowanie
    # --------------------------
    def stealth_setup(self):
        self.page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            window.navigator.chrome = {runtime:{}};
            Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3,4,5]});
            Object.defineProperty(navigator, 'languages', {get: () => ['en-US','en']});
        """)

    # --------------------------
    # Klikanie elementów
    # --------------------------
    def click_element_by_selector(self, selector: str):
        try:
            el = self.page.locator(selector)
            el.wait_for(state="visible", timeout=10000)
            box = el.bounding_box()
            if box:
                self._move_mouse_random(box)
            el.click()
            print(f"[CLICK] Element selector: {selector}")
            self._human_delay()
        except Exception as e:
            print(f"[ERROR CLICK] Selector '{selector}': {e}")

    def click_element_by_text(self, text: str):
        try:
            el = self.page.locator(f"text={text}")
            el.wait_for(timeout=10000)
            box = el.bounding_box()
            if box:
                self._move_mouse_random(box)
            el.click()
            print(f"[CLICK] Text: {text}")
            self._human_delay()
        except Exception as e:
            print(f"[ERROR CLICK] Text '{text}': {e}")

    def click_element_fullpath(self, target: str):
        try:
            # Jeśli wygląda na selektor CSS (np. zawiera nawiasy kwadratowe, kropki, dwukropki itp.)
            if any(sym in target for sym in ['[', '.', ':', '#', '>']):
                el = self.page.locator(target)
                print(f"[LOCATOR] Using CSS selector: {target}")
            else:
                el = self.page.locator(f"text={target}")
                print(f"[LOCATOR] Using text selector: {target}")

            el.wait_for(timeout=10000)
            box = el.bounding_box()
            if box:
                self._move_mouse_random(box)
            el.click()
            print(f"[CLICK] Target: {target}")
            self._human_delay()
        except Exception as e:
            print(f"[ERROR CLICK] Target '{target}': {e}")

    def click_element_by_xpath(self, xpath: str):
        try:
            el = self.page.locator(f'xpath={xpath}')
            el.wait_for(timeout=10000)
            box = el.bounding_box()
            if box:
                self._move_mouse_random(box)
            el.click()
            print(f"[CLICK] XPath: {xpath}")
            self._human_delay()
        except Exception as e:
            print(f"[ERROR CLICK] XPath '{xpath}': {e}")

    def is_element_visible(self, selector: str) -> bool:
        try:
            el = self.page.locator(selector)
            el.wait_for(timeout=5000, state="visible")
            print(f"[VISIBLE] Element is visible: {selector}")
            return True
        except Exception as e:
            print(f"[NOT VISIBLE] Element not visible: {selector} — {e}")
            return False


    # --------------------------
    # Hover nad elementem
    # --------------------------
    def hover_element_by_selector(self, selector: str):
        try:
            el = self.page.locator(selector)
            el.wait_for(state="visible", timeout=5000)
            box = el.bounding_box()
            if box:
                self._move_mouse_random(box)
            el.hover()
            print(f"[HOVER] Selector: {selector}")
            self._human_delay()
        except Exception as e:
            print(f"[ERROR HOVER] Selector '{selector}': {e}")

    def hover_element_by_xpath(self, xpath: str):
        try:
            el = self.page.locator(f'xpath={xpath}')
            el.wait_for(state="visible", timeout=5000)
            box = el.bounding_box()
            if box:
                self._move_mouse_random(box)
            el.hover()
            print(f"[HOVER] XPath: {xpath}")
            self._human_delay()
        except Exception as e:
            print(f"[ERROR HOVER] XPath '{xpath}': {e}")



    def hover_element_by_text(self, text: str):
        try:
            el = self.page.locator(f"text={text}")
            el.wait_for(timeout=5000)
            box = el.bounding_box()
            if box:
                self._move_mouse_random(box)
            el.hover()
            print(f"[HOVER] Text: {text}")
            self._human_delay()
        except Exception as e:
            print(f"[ERROR HOVER] Text '{text}': {e}")

    # --------------------------
    # Pisanie tekstu
    # --------------------------
    def type_text_in_field(self, selector: str, text: str):
        try:
            field = self.page.locator(selector)
            field.wait_for(state="visible", timeout=10000)
            field.click()
            field.fill("")
            for char in text:
                field.type(char)
                self._human_delay(0.05, 0.15)
            print(f"[TYPE] '{text}' into {selector}")
        except Exception as e:
            print(f"[ERROR TYPE] Selector '{selector}': {e}")

    def type_text_using_keyboard(self, text: str):
        try:
            self.page.focus("body")
            for char in text:
                self.page.keyboard.press(char)
                self._human_delay(0.05, 0.15)
            print(f"[TYPE KEYBOARD] '{text}'")
        except Exception as e:
            print(f"[ERROR TYPE KEYBOARD] '{text}': {e}")

    # --------------------------
    # Scrollowanie
    # --------------------------
    def scroll_page_steps(self, steps=3, distance=700, delay=0.8):
        try:
            for i in range(steps):
                self.page.mouse.wheel(0, distance)
                self.page.mouse.move(random.randint(100, 800), random.randint(100, 600))
                self._human_delay(delay, delay + 0.5)
                print(f"[SCROLL] Step {i+1}, distance {distance}")
        except Exception as e:
            print(f"[ERROR SCROLL]: {e}")

    # --------------------------
    # Ładowanie strony
    # --------------------------
    def load_page(self, url: str):
        try:
            self.page.goto(url, timeout=20000)
            print(f"[LOAD PAGE] {url}")
            self._human_delay(1, 2)
            for _ in range(random.randint(1, 2)):
                self.page.mouse.wheel(0, random.randint(200, 500))
                self._human_delay(0.3, 0.7)
        except Exception as e:
            print(f"[ERROR LOAD PAGE] {url}: {e}")

    # --------------------------
    # Funkcje pomocnicze
    # --------------------------
    def _move_mouse_random(self, box):
        x = box["x"] + box["width"] * random.uniform(0.3, 0.7)
        y = box["y"] + box["height"] * random.uniform(0.3, 0.7)
        self.page.mouse.move(x, y)
