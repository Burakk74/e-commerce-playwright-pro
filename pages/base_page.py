from data.config import Config
from playwright.async_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = Config.BASE_URL

    async def navigate(self, path: str = ""):
        await self.page.goto(f"{self.base_url}{path}")

    async def click_element(self, selector: str):
        # Elementin hazır olmasını bekleyip tıklar
        await self.page.wait_for_selector(selector, state="visible")
        await self.page.click(selector)

    async def fill_field(self, selector: str, text: str):
        # Elementin hazır olmasını bekleyip içini doldurur
        await self.page.wait_for_selector(selector, state="visible")
        await self.page.fill(selector, text)