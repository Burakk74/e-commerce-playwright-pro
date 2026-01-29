# pages/login_page.py

from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._email_input = "#input-email"
        self._password_input = "#input-password"
        self._login_btn = "input[value='Login']"
        self._error_msg = ".alert-danger"
        # My Account sayfası doğrulaması için
        self._account_side_nav = "#column-right" 

    async def login(self, email, password):
        await self.fill_field(self._email_input, email)
        await self.fill_field(self._password_input, password)
        await self.click_element(self._login_btn)

    async def get_error_message(self):
        locator = self.page.locator(self._error_msg)
        await locator.wait_for(state="visible", timeout=5000)
        text = await locator.text_content()
        return text.strip() 