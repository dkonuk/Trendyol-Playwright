from playwright.sync_api import Page


class BasePage:
    def __init__(self, page):
        self.page = page

        self.onboarding_pop_up = self.page.get_by_text("Aradığın Tüm Kategoriler")
        self.onboarding_popup_close = self.page.locator("#navigation-wrapper span").nth(1)

    def get_title(self):
        return self.page.title()

    def check_onboarding_popup(self):
        if self.onboarding_pop_up.is_visible():
            self.onboarding_popup_close.click()


