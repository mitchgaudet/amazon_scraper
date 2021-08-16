import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.ca/dp/B075SDMMMV/?coliid=I1KWOLZK5853Z6&colid=R0D3SGRJCV5I&psc=1&ref_=lv_ov_lig_dp_it'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[5:8])

    title = soup.find(id="productTitle").get_text()

    if(converted_price < 800):
        send_mail()

    print(title.strip())
    print(converted_price)

    if(converted_price < 800):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mitchellrgaudet@gmail.com', 'zxedjirhbsanfqrp')

    subject = 'Price fell down!'
    body = 'Check the Amazon link https://www.amazon.ca/dp/B075SDMMMV/?coliid=I1KWOLZK5853Z6&colid=R0D3SGRJCV5I&psc=1&ref_=lv_ov_lig_dp_it'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mitchellrgaudet@gmail.com',
        'gaudet186@hotmail.ca',
        msg
    )
    print('HEY, THE EMAIL WAS SENT')

    server.quit()

while(True):
    check_price()
    time.sleep(86400)