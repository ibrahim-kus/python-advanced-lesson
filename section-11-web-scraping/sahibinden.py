from bs4 import BeautifulSoup
import requests

# Hedef URL
url = "https://www.sahibinden.com/satilik-arsa/antalya"

# Kullanıcı ajanı başlığı (bot olarak algılanmayı önlemek için)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Sayfayı indirme
response = requests.get(url, headers=headers)

# HTTP durum kodunu kontrol etme
if response.status_code == 200:
    # BeautifulSoup ile HTML içeriğini işleme
    soup = BeautifulSoup(response.text, "html.parser")

    # İlan kartlarını seçme
    cards = soup.find_all("div", class_="searchResultsItem")

    # Kartlardan başlıkları alma
    for card in cards:
        title = card.find("a", class_="classifiedTitle")
        if title:
            print("İlan Başlığı:", title.text.strip())
else:
    print("Sayfa yüklenemedi. HTTP Durum Kodu:", response.status_code)
