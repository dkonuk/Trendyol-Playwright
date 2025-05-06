import pytest
import time
from pages.HomePage import HomePage
from playwright.sync_api import Page

def test_github(page : Page):
    homepage = HomePage(page)
    homepage.navigate()