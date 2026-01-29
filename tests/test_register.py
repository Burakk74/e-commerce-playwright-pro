import pytest
from faker import Faker
from pages.register_page import RegisterPage

fake = Faker()

@pytest.mark.asyncio
async def test_successful_registration(page):
    register_page = RegisterPage(page)
    await register_page.navigate("index.php?route=account/register")
    
    # Rastgele veriler oluşturuyoruz
    email = fake.email()
    password = "TestPassword123!"
    
    await register_page.register_new_user(
        fake.first_name(), 
        fake.last_name(), 
        email, 
        "5554443322", 
        password
    )
    
    # Başarı mesajını kontrol et
    success_text = await register_page.get_success_message()
    assert "Your Account Has Been Created!" in success_text
    
    # İleride valid_login testinde kullanmak istersen bu email/şifreyi bir yere loglayabilirsin
    print(f"\nYeni oluşturulan kullanıcı: {email} / {password}")