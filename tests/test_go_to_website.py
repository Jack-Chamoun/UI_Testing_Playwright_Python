from playwright.sync_api import expect
from objectrepository.Home import Home
from objectrepository.mestery import Mestery

class Test_go_to_website:
    def test_go_to_website(self, page):
        page.goto("https://books.toscrape.com/")
        expect(page.get_by_role("alert")).to_contain_text("Warning! This is a demo website for web scraping purposes. Prices and ratings here were randomly assigned and have no real meaning.")
        expect(page.get_by_role("banner")).to_contain_text("Books to Scrape")
        page.wait_for_timeout(2000)
        page.locator(Home.MESTERY_BUTTON).click()
        page.wait_for_timeout(2000)
        expect(page.locator(Mestery.MESTERY_PAGE_TITLE)).to_be_visible()