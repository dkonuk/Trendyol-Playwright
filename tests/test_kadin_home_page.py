from pages.HomePage import HomePage
from pages.KadinHomePage import KadinHomePage
from playwright.sync_api import Page

def test_kadin_home_page(page: Page):
    kadin_homepage = KadinHomePage(page)
    kadin_homepage.navigate()
    kadin_homepage.click_sepete_en_cok_eklenenler()
    page.go_back()
    kadin_homepage.click_one_cikanlar()
    page.go_back()
    kadin_homepage.click_flas_urunler()
    page.go_back()
    kadin_homepage.click_kampanya_detaylari()