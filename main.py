
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
"""
1 - https://www.lcwaikiki.com/tr-TR/TR adresine git.
2 - Çerezleri kabul et butonuna bas.
3 - Aksesuar kategorisinden çok satanlara gir.
4 - Ürün seç.
5 - Sepete ekle. 
6 - Sepete git.
7 - Anasayfaya dön.
"""

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Adrese ulaşıyoruz
driver.get("https://www.lcwaikiki.com/tr-TR/TR")

#Tam ekran için
driver.maximize_window()
time.sleep(3)

#Locators

# Tüm çerezleri kabul et
cookie = driver.find_element(By.XPATH, "//*[@id='cookieseal-banner']/div/button[2]")
assert cookie is not None, "Öğe bulunamadı."
print("Cookie bulundu.")
cookie.click()
time.sleep(2)

#Aksesuar kategorisine git
category = driver.find_element(By.LINK_TEXT, 'AKSESUAR')
assert category is not None, "Öğe bulunamadı."
print("category bulundu.")
category.click()
time.sleep(2)

#Çok satanlara gir
cokSatanlar = driver.find_element(By.XPATH, "//div[@class='tekli-1 flexcontainer']")
assert cokSatanlar is not None, "Öğe bulunamadı."
print("cokSatanlar bulundu.")
cokSatanlar.click()
time.sleep(2)

#Scroll down
driver.execute_script("window.scrollTo(0, 250)")
time.sleep(2)

#Ürüne git
urunSayfasi = driver.find_element(By.CSS_SELECTOR, ".product-card:nth-child(2) .product-card__title")
assert urunSayfasi is not None, "Öğe bulunamadı."
print("Ürün bulundu.")
urunSayfasi.click()
time.sleep(2)

#Sepete ekleme
sepeteEkle = driver.find_element(By.XPATH, "//a[@id='pd_add_to_cart']")
assert sepeteEkle is not None, "Öğe bulunamadı."
print("sepeteEkle bulundu.")
sepeteEkle.click()
time.sleep(2)

#Sepete git
sepeteGit = driver.find_element(By.XPATH, "//span[text()='Sepetim']")
assert sepeteGit is not None, "Öğe bulunamadı."
print("sepeteGit bulundu.")
sepeteGit.click()
time.sleep(2)

#Anasayfaya dön
anasayfa = driver.find_element(By.XPATH, "//a[@class='main-header-logo']")
assert anasayfa is not None, "Öğe bulunamadı."
print("anasayfa bulundu.")
anasayfa.click()

driver.close()
