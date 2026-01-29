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