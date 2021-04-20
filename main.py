from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

URL = "https://www.amazon.com.br/SSD-SATA3-120GB-Kingston-SA400S37/dp/B01N6JQS8C/ref=asc_df_B01N6JQS8C/?tag=googleshopp00-20&linkCode=df0&hvadid=379713309483&hvpos=&hvnetw=g&hvrand=11063542056456285281&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1031586&hvtargid=pla-318932234081&psc=1"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77"
ACCEPT_LANG = "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"

my_email = "teste.teste@gmail.com"
password = "abcd1234"

response = requests.get(URL, headers={"User-Agent": USER_AGENT, "Accept-Language": ACCEPT_LANG})

website_html = response.content

soup = BeautifulSoup(website_html, "lxml")

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency.replace(',', '.'))
product_name = soup.find(id="productTitle").get_text()
print(price_as_float)
print(product_name)

if price_as_float < 200:
    mensagem = f"{product_name} agora tem o preço de R${price_as_float}"

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Amazon Price Tracker!\n\n{mensagem}\n{URL}")
