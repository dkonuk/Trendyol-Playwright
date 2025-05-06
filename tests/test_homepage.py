import pytest
import time
from pages.HomePage import HomePage
from playwright.sync_api import Page

def test_homepage(page: Page):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.accept_cookies()
    homepage.test_major_navigation_links()
    homepage.navigate()






