import requests
from bs4 import BeautifulSoup
import pandas as pd

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "https://10.10.1.10:1080"
}

data = {'Title': [],
        'Price': [],
        'Image': []}

url = "https://www.amazon.in/s?k=iphones&crid=2V86TE8OVY1XC&sprefix=iphone%2Caps%2C495&ref=nb_sb_noss_2"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price-whole")
images = soup.select("img.s-image")

for span in spans:
    # print(span.get_text())
    title = span.string.strip() if span.string else "product-title"
    data["Title"].append(title)

for price in prices:
    # print(price.get_text())
    price_value = price.string.strip() if price.string else "price-of-product"
    data["Price"].append(price_value)

for image in images:
    # print(image.get("src"))
    image_src = image.get("src") if image.get("src") else "Image-url"
    data["Image"].append(image_src)

print(f'url={len(images)}\ntitles={len(spans)}\nprices={len(prices)}')

# Check if all lists have the same length before creating the DataFrame
if len(data["Title"]) == len(data["Price"]) == len(data["Image"]):
    df = pd.DataFrame(data)
    df.to_csv("data.csv", index=False)
else:
    print("The lists have different lengths, cannot create DataFrame.")
