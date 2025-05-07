from pages.AnneCocukHomePage import AnneCocukHomePage
from playwright.sync_api import Page


def test_anne_cocuk_home_page(page: Page):
    anne_cocuk_page = AnneCocukHomePage(page)
    anne_cocuk_page.navigate()
    anne_cocuk_page.click_cok_satanlar()
    page.go_back()
    anne_cocuk_page.click_bebek()
    page.go_back()
    anne_cocuk_page.click_kiz_cocuk()
    page.go_back()
    anne_cocuk_page.click_erkek_cocuk()
    page.go_back()
    anne_cocuk_page.click_oyuncak()
    page.go_back()
    anne_cocuk_page.click_bebek_bezi()
    page.go_back()
    anne_cocuk_page.click_ayakkabi()