from playwright.sync_api import Page

class ErkekHomePage:
    ErkekHomePageURL = "https://www.trendyol.com/butik/liste/2/erkek"


    def __init__(self, page: Page):
        self.page = page

        self.sepete_en_cok_eklenenler = self.page.get_by_role("link", name="Sepete En Çok Eklenenler")
        self.one_cikanlar = self.page.get_by_role("link", name="En Çok Öne Çıkanlar")
        self.flas_urunler = self.page.get_by_role("link", name="Flaş Ürünler").first
        self.kampanya_detaylari = self.page.get_by_role("link", name="Kampanya Detayları")

    def navigate(self):
        self.page.goto(self.ErkekHomePageURL)

    def click_sepete_en_cok_eklenenler(self):
        self.sepete_en_cok_eklenenler.click()

    def click_one_cikanlar(self):
        self.one_cikanlar.click()

    def click_flas_urunler(self):
        self.flas_urunler.click()

    def click_kampanya_detaylari(self):
        self.kampanya_detaylari.click()