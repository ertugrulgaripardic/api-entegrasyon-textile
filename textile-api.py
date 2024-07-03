import requests
import json

# Sağlanan aktif token
token = "39|5oxXwOVIrpE1R0851aRxp3NIkLujvZo0NqmI29FR"

# Token'ı Authorization header'ına eklemek
headers = {
    "Authorization": f"Bearer {token}"
}

# Stok kartlarını çekmek için URL ve parametreler
stocks_url = "http://api.redex.com.tr/meta/cards/stocks/outside"
params = {
    "warehouseCode": "DEPO1",
    "priceListNoAndCurrencyUnit": "0,USD",
    "page": 3
}

try:
    # GET isteği ile stok kartlarını çekmek
    response = requests.get(stocks_url, headers=headers, params=params)
    response.raise_for_status()  # Bu satır, HTTP hata kodlarını yakalamak için eklendi
    stock_cards = response.json()

    # JSON verisini dosyaya kaydetmek
    with open("stock_cards.json", "w", encoding="utf-8") as file:
        json.dump(stock_cards, file, ensure_ascii=False, indent=4)

    print("Stok kartları başarıyla 'stock_cards.json' dosyasına kaydedildi.")
except requests.exceptions.RequestException as e:
    print("Stok kartlarını çekme başarısız:", e)
