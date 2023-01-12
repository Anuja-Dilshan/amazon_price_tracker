import requests
from bs4 import BeautifulSoup
import smtplib

USER = ''
PASSWORD = ""
PRODUCT_URL = 'https://www.amazon.com/Smart-Watch-Men-Women-Fitness/dp/B0BG9VW8JL/ref=sr_1_1_sspa?th=1'

amazon_headers = {
    "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Request Line": "GET/HTTP/1.1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Connection":"keep-alive",



}

response = requests.get(url=PRODUCT_URL,
                        headers=amazon_headers)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, 'html.parser')
name = soup.select_one("#productTitle").get_text().strip(' ')
price = soup.select_one(".a-price-whole").get_text()
cents = soup.select_one('.a-price-fraction').get_text()
current_price = float(f"{price}{cents}")

if current_price <= 35.00:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER, to_addrs=USER, msg=f"subject: LOW PRICE ALERT!!\n\nProduct Name: {name}\nhas been "
                                                               f"lowered upto $35.00 buy it today")



