import pytest
from playwright.async_api import expect  
from pages.cart_page import CartPage

@pytest.mark.asyncio
async def test_add_product_to_cart(page):
    cart_page = CartPage(page)
    await cart_page.navigate()
    await cart_page.search_and_add_to_cart("iPhone")
    
    # Toast mesajını doğrula (Doğru kullanım: expect(locator))
    success_toast = page.locator("#notification-box-top")
    await expect(success_toast).to_contain_text("Success")
     
    # Badge değerinin "0" olmadığını doğrula
    badge = page.locator(".cart-icon .badge").first
    await expect(badge).not_to_have_text("0")
    
    count = await badge.text_content()
    assert int(count) > 0