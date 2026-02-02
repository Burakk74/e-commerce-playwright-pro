🛒 E-COMMERCE-PLAYWRIGHT-PRO
Bu proje, LambdaTest eCommerce Playground platformu üzerinde uçtan uca kullanıcı senaryolarını test etmek için geliştirilmiş, Python tabanlı ve Page Object Model (POM) mimarisini kullanan modern bir asenkron test otomasyon framework'üdür.

Framework, yüksek performanslı ve sürdürülebilir test süreçleri sağlamak amacıyla Playwright'ın asenkron yeteneklerinden yararlanır.

🛠 Kullanılan Teknolojiler
Python 3.13+: Temel programlama dili.

Playwright (Async): Modern, hızlı ve güvenilir tarayıcı otomasyonu.

PyTest: Test framework'ü ve senaryo yönetimi.

Faker: Dinamik ve gerçekçi test verisi üretimi.

Dotenv: Hassas verilerin (.env) güvenli yönetimi.

Pytest-HTML: Test sonuçlarını görselleştirmek için raporlama aracı.

🏗 Proje Mimarisi
Framework, kodun tekrar kullanılabilirliğini ve kolay bakımını sağlamak amacıyla Page Object Model (POM) prensiplerine göre yapılandırılmıştır:

pages/: Web sayfalarındaki elementlerin ve bu elementlerle yapılan aksiyonların (click, fill vb.) tanımlandığı katman.

tests/: Gerçek test senaryolarının (Pozitif ve Negatif) bulunduğu katman.

data/: Yapılandırma ayarlarının ve ortam değişkenlerinin yönetildiği katman.

conftest.py: Test öncesi kurulum (setup) ve fixture'ların yönetildiği merkez.

📋 Test Senaryoları
Kayıt Testi: Faker kütüphanesi ile her seferinde benzersiz kullanıcı verileri üretilerek yeni hesap oluşturma süreci doğrulanır.

Giriş Testleri:

Pozitif: Geçerli bilgilerle başarılı giriş ve profil sayfasına yönlendirme kontrolü.

Negatif: Hatalı bilgiler veya güvenlik sınırları (rate limit) durumunda doğru hata mesajlarının alındığının doğrulanması.

Sepet İşlemleri: Ürün arama, sonuç listesinden ürün seçimi, sepete ekleme ve sepet ikonundaki dinamik sayı değişiminin doğrulanması.

🚀 Kurulum ve Çalıştırma
Projenizi yerel ortamda çalıştırmak için şu adımları izleyin:

1. Projeyi klonlayın:

Bash
git clone https://github.com/KULLANICI_ADIN/ecommerce-playwright-project.git
cd ecommerce-playwright-project
2. Sanal ortam oluşturun ve aktif edin:

Bash
python -m venv venv
.\venv\Scripts\activate  # Windows için
source venv/bin/activate # Linux/Mac için
3. Bağımlılıkları ve tarayıcıları yükleyin:

Bash
pip install -r requirements.txt
playwright install
4. Testleri çalıştırın ve rapor oluşturun:

Bash
pytest --html=rapor.html --self-contained-html
📊 Raporlama
Testler tamamlandığında proje dizininde oluşan rapor.html dosyasını herhangi bir tarayıcı ile açarak detaylı test sonuçlarını, çalışma sürelerini ve varsa hata loglarını görebilirsiniz.



EN

🛒 E-COMMERCE-PLAYWRIGHT-PRO
This project is a modern, Python-based asynchronous test automation framework designed to test end-to-end user scenarios on the LambdaTest eCommerce Playground platform. It utilizes the Page Object Model (POM) architecture to ensure scalability and maintainability.

The framework leverages the asynchronous capabilities of Playwright to provide high-performance and sustainable testing processes.

🛠 Tech Stack
Python 3.13+: Core programming language.

Playwright (Async): Modern, fast, and reliable browser automation.

PyTest: Test framework and scenario management.

Faker: Generation of dynamic and realistic test data.

Dotenv: Secure management of sensitive data via .env files.

Pytest-HTML: Reporting tool for visualizing test results.

🏗 Project Architecture
The framework is structured according to Page Object Model (POM) principles to ensure code reusability and easy maintenance:

pages/: The layer where web elements and page-specific actions (click, fill, etc.) are defined.

tests/: The layer containing actual test scenarios (Positive and Negative).

data/: Management of configuration settings and environment variables.

conftest.py: The central hub for test setup, teardown, and fixture management.

📋 Test Scenarios
Registration Test: Validates the account creation process using the Faker library to generate unique user data for every execution.

Login Tests:

Positive: Verifies successful login with valid credentials and redirection to the profile page.

Negative: Verifies that correct error messages are displayed for invalid credentials or security constraints (e.g., rate limits).

Cart Operations: Includes product searching, selecting items from results, adding to the cart, and validating dynamic badge updates on the cart icon.

🚀 Installation and Execution
Follow these steps to run the project in your local environment:

1. Clone the project:

Bash
git clone https://github.com/YOUR_USERNAME/ecommerce-playwright-project.git
cd ecommerce-playwright-project
2. Create and activate a virtual environment:

Bash
python -m venv venv
# For Windows:
.\venv\Scripts\activate  
# For Linux/Mac:
source venv/bin/activate 
3. Install dependencies and browsers:

Bash
pip install -r requirements.txt
playwright install
4. Run tests and generate a report:

Bash
pytest --html=report.html --self-contained-html
📊 Reporting
Once the tests are complete, you can open the report.html file generated in the project directory using any web browser. This report provides detailed test results, execution times, and error logs if any failures occurred.