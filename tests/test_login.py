import re
import pytest
from pages.login_page import LoginPage
from data.config import Config
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_valid_login_scenario(page):
    login_page = LoginPage(page)
    
    # URL'i Config'den alıyoruz
    await login_page.navigate("index.php?route=account/login")
    
    # Verileri Config'den alıyoruz
    await login_page.login(Config.USER_EMAIL, Config.PASSWORD)
    
    # expect altındaki sarı çizgi devam ederse, page objesi üzerinden doğrula:
    await expect(page).to_have_url(re.compile(r".*route=account/account"))
    
    # Sağ menü kontrolü
    side_menu = page.locator("#column-right")
    await expect(side_menu).to_be_visible()


@pytest.mark.asyncio
async def test_invalid_login_scenario(page):
    login_page = LoginPage(page)
    # Login sayfasına git
    await login_page.navigate("index.php?route=account/login")
     
    # Hatalı giriş dene
    await login_page.login("yanlis@mail.com", "123456")
     
    # Hata mesajını al
    error = await login_page.get_error_message()
    
    # PROFESYONEL GÜNCELLEME:
    # Hem normal "hatalı giriş" mesajını hem de "çok fazla deneme" (rate limit) mesajını kabul ediyoruz.
    # Böylece site seni bloklasa bile testin "logic" olarak doğru çalıştığını teyit ederiz.
    expected_msg_1 = "Warning: No match for E-Mail Address and/or Password."
    expected_msg_2 = "Warning: Your account has exceeded allowed number of login attempts."
    
    assert (expected_msg_1 in error or expected_msg_2 in error), f"Beklenen hata mesajı alınamadı. Gelen mesaj: {error}"