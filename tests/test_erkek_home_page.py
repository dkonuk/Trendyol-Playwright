from pages.ErkekHomePage import ErkekHomePage
from playwright.sync_api import Page
import time

def test_erkek_home_page(page: Page):
    erkek_homepage = ErkekHomePage(page)
    erkek_homepage.navigate()
    time.sleep(2)
    erkek_homepage.click_sepete_en_cok_eklenenler()
    page.go_back()
    erkek_homepage.click_one_cikanlar()
    page.go_back()
    erkek_homepage.click_flas_urunler()
    page.go_back()
    erkek_homepage.click_kampanya_detaylari()