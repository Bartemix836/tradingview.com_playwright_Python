import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=300)
        context = browser.new_context(
            viewport={"width": 1500, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # Oddajemy fixture testowi
        yield {"browser": browser, "context": context, "page": page}

        # ⚠️ Wywołanie input() działa tylko, jeśli pytest uruchomiony z -s
        # input("Naciśnij Enter, aby zamknąć przeglądarkę i zakończyć test...")
        context.close()
        browser.close()
