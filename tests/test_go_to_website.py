from playwright.sync_api import expect
from objectrepository.home import Home
from objectrepository.mestery import Mestery

class Test_go_to_website:
    def test_go_to_website(self, page):
        page.goto("https://books.toscrape.com/") # here the URL should be from .env file for easier configuration and to make the confiurations in one place
        expect(page.get_by_role("alert")).to_contain_text("Warning! This is a demo website for web scraping purposes. Prices and ratings here were randomly assigned and have no real meaning.")
        expect(page.get_by_role("banner")).to_contain_text("Books to Scrape")
        page.locator(Home.MESTERY_BUTTON).click()
        expect(page.locator(Mestery.MESTERY_PAGE_TITLE)).to_be_visible()
        