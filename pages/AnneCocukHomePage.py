from playwright.sync_api import Page

class AnneCocukHomePage:
    AnneCocukHomePageURL = "https://www.trendyol.com/butik/liste/3/anne-cocuk"
    def __init__(self, page: Page):
        self.page = page

        self.cok_satanlar = self.page.get_by_role("link", name="Çok Satanlar").first
        self.bebek = self.page.get_by_role("link", name="Bebek").first
        self.kız_cocuk = self.page.get_by_role("link", name="Kız Çocuk", exact=True)
        self.erkek_cocuk = self.page.get_by_role("link", name="Erkek Çocuk", exact=True)
        self.oyuncak = self.page.get_by_role("link", name="Oyuncak", exact=True)
        self.bebek_bezi = self.page.get_by_role("link", name="Bebek Bezi", exact=True).first
        self.ayakkabi = self.page.get_by_role("link", name="Ayakkabı", exact=True)
        self.banyo_tuvalet = self.page.get_by_role("link", name="Banyo & Tuvalet", exact=True)
        self.beslenme = self.page.get_by_role("link", name="Beslenme", exact=True)
        self.cocuk_gerec = self.page.get_by_role("link", name="Çocuk Gereç", exact=True)
        self.cocuk_kitaplari = self.page.get_by_role("link", name="Çocuk Kitapları")


    def navigate(self):
        self.page.goto(self.AnneCocukHomePageURL)

    def click_cok_satanlar(self):
        self.cok_satanlar.click()

    def click_bebek(self):
        self.bebek.click()

    def click_kiz_cocuk(self):
        self.kız_cocuk.click()

    def click_erkek_cocuk(self):
        self.erkek_cocuk.click()

    def click_oyuncak(self):
        self.oyuncak.click()

    def click_bebek_bezi(self):
        self.bebek_bezi.click()

    def click_ayakkabi(self):
        self.ayakkabi.click()

    def click_banyo_tuvalet(self):
        self.banyo_tuvalet.click()

    def click_beslenme(self):
        self.beslenme.click()

    def click_cocuk_gerec(self):
        self.cocuk_gerec.click()

    def click_cocuk_kitaplari(self):
        self.cocuk_kitaplari.click()