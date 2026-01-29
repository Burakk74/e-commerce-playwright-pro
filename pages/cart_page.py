from pages.base_page import BasePage
from playwright.async_api import expect

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._search_input = "input[name='search']"
        self._search_btn = ".type-text"
        self._first_product = ".product-layout"
        self._add_to_cart_btn = "button[title='Add to Cart']"
        # Görseldeki sağ üstte çıkan toast mesajı için yeni locator
        self._toast_msg = "#notification-box-top .toast-body" 
        self._cart_total_badge = ".cart-icon .badge"

    async def search_and_add_to_cart(self, product_name: str):
        await self.fill_field(self._search_input, product_name)
        await self.click_element(self._search_btn)
        
        product = self.page.locator(self._first_product).first
        await product.hover()
        await product.locator(self._add_to_cart_btn).click()
        
        # Toast beklemek yerine, sepetin 0'dan farklı bir sayıya dönmesini bekle (Daha stabil)
        badge = self.page.locator(".cart-icon .badge").first
        await expect(badge).not_to_have_text("0", timeout=10000)