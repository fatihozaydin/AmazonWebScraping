import requests
from bs4 import BeautifulSoup

def scrape_amazon_product_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Ürün adını çek
        product_title = soup.find('span', {'id': 'productTitle'})
        if product_title:
            product_title = product_title.get_text(strip=True)
        else:
            product_title = 'Ürün adı bulunamadı'
        
        # Ürün fiyatını çek
        product_price = soup.find('span', {'class': 'a-price-whole'})
        if product_price:
            product_price = product_price.get_text(strip=True)
            product_price_fraction = soup.find('span', {'class': 'a-price-fraction'})
            if product_price_fraction:
                product_price += product_price_fraction.get_text(strip=True)
        else:
            product_price = 'Ürün fiyatı bulunamadı'

        product_score = soup.find('span', {'class': 'a-icon-alt'})
        if product_score:
            product_score = product_score.get_text(strip=True)
        else:
            product_score = 'Ürün adı bulunamadı'


        product_comment = soup.find('span', {'id': 'acrCustomerReviewText'})
        if product_comment:
            product_comment = product_comment.get_text(strip=True)
        else:
            product_comment = 'Ürün adı bulunamadı'
        
        print(f"Ürün Adı: {product_title}")
        print(f"Ürün Fiyatı: {product_price}","TL")
        print(f"Ürün Skoru: {product_score}")
        print(f"Ürün Yorumları: {product_comment}")
    else:
        print(f"Web sayfasına erişim sağlanamadı. Durum kodu: {response.status_code}")

if __name__ == "__main__":
    product_url = input("Lütfen linki girin: ")
    scrape_amazon_product_info(product_url)
