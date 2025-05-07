from playwright.sync_api import Page
from pages.BasePage import BasePage


class HomePage(BasePage):
    URL = "https://www.trendyol.com/"
    main_navigation_links = {
        "Kadın": "/kadin",
        "Erkek": "/erkek",
        "Anne & Çocuk": "/anne-cocuk",
        "Ev & Yaşam": "/ev-yasam",
        "Süpermarket": "/supermarket",
        "Kozmetik": "/kozmetik",
        "Ayakkabı & Çanta": "/ayakkabi-canta",
        "Elektronik": "/elektronik",
        "Çok Satanlar Yeni": "/cok-satanlar"
    }


    def __init__(self, page: Page):
        self.page = page

        self.accept_cookies_button = page.locator("#onetrust-accept-btn-handler")
        self.navbar_kadin = page.get_by_role("link", name="Kadın", exact=True)
        self.onboarding_pop_up = page.get_by_text("Aradığın Tüm Kategoriler")
        self.onboarding_popup_close =self.page.locator("#navigation-wrapper span").nth(1)


    def navigate(self):
        self.page.goto(HomePage.URL)


    def accept_cookies(self):
        self.accept_cookies_button.wait_for(state="visible")
        self.accept_cookies_button.click()

    def test_major_navigation_links(self):
        for link_text, expected_path in self.main_navigation_links.items():
            self.check_onboarding_popup()
            element = self.page.get_by_role("link", name=link_text, exact=True)
            self.check_onboarding_popup()
            element.click()
            assert expected_path in self.page.url, f"{expected_path} not found in {self.page.url}"
            self.page.go_back()


