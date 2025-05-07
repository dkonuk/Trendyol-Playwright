from playwright.sync_api import Page


class KadinHomePage:
    KadinHomePageURL = "https://www.trendyol.com/butik/liste/1/kadin"


    def __init__(self, page: Page):
        self.page = page

        self.sepete_en_cok_eklenenler = self.page.get_by_role("link", name="Sepete En Çok Eklenenler")
        self.one_cikanlar = self.page.get_by_role("link", name="En Çok Öne Çıkanlar")

    def navigate(self):
        self.page.goto(self.KadinHomePageURL)

    def click_sepete_en_cok_eklenenler(self):
        self.sepete_en_cok_eklenenler.click()

    def click_one_cikanlar(self):
        self.one_cikanlar.click()