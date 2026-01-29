from pages.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._firstname = "#input-firstname"
        self._lastname = "#input-lastname"
        self._email = "#input-email"
        self._telephone = "#input-telephone"
        self._password = "#input-password"
        self._confirm = "#input-confirm"
        self._agree_chkbx = "label[for='input-agree']"
        self._continue_btn = "input[value='Continue']"
        self._success_msg = "#content h1"

    async def register_new_user(self, fname, lname, email, phone, password):
        await self.fill_field(self._firstname, fname)
        await self.fill_field(self._lastname, lname)
        await self.fill_field(self._email, email)
        await self.fill_field(self._telephone, phone)
        await self.fill_field(self._password, password)
        await self.fill_field(self._confirm, password)
        await self.page.click(self._agree_chkbx)
        await self.click_element(self._continue_btn)

    async def get_success_message(self):
        return await self.page.locator(self._success_msg).text_content()