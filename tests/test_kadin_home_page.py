from pages.HomePage import HomePage
from pages.KadinHomePage import KadinHomePage
from playwright.sync_api import Page

def test_kadin_home_page(page: Page):
    kadin_homepage = KadinHomePage(page)
    kadin_homepage.navigate()
    kadin_homepage.click_sepete_en_cok_eklenenler()