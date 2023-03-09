import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv


# homepage all sub categories
# for every link get the firsts products page 1 then get link for next page get products
products_names = []
product_images = []
product_prices = []
product_discounts = []

url = "https://www.jumia.co.ke/soccer-sports-accessories/"
page = requests.get(url, timeout=20)
soup = BeautifulSoup(page.content, "html.parser")
if soup is not None:
    sub_category4_data = soup.find_all("a", class_="core")
    if sub_category4_data is not None:

        for data in sub_category4_data:
            # print("data available", data.prettify())
            image = data.find("img", class_="img")

            img_link = image["data-src"]
            product_name = data.find("h3", class_="name").get_text()
            product_price = data.find("div", class_="prc").get_text()
            product_discount = data.find("div", class_="_dsct")
            if product_discount is not None:
                product_discount = product_discount.get_text()

            # print("product discount", product_discount)

            text = data.get_text()
            link = data.get("href")
            if link is not None:
                product_prices.append(product_price)
                products_names.append(product_name)
                product_discounts.append(product_discount)
                product_images.append(img_link)
               

    # loop pages get links
     # if page next get page next in next page
    # loop pages till arai-label is Last Page
    pages_toloop = None
    page_urls = []

    if soup is not None:
        pages = soup.find_all("a", class_="pg")
        for page in pages:
            if page.get("aria-label") == "Last Page":

                page_link = page.get("href")
                pages_toloop = int(page_link.split("=")[1][:2])

                if "http" not in page_link:
                    page_link = "https://www.jumia.co.ke/" + page_link

                for x in range(2, pages_toloop+1):
                    url = f'https://www.jumia.co.ke/soccer-sports-accessories/?page={x}#catalog-listing'
                    page_urls.append(url)

    for pagelink in page_urls:
        # # use page links to get products
        url = pagelink
        page = requests.get(url, timeout=20)
        soup = BeautifulSoup(page.content, "html.parser")
        pages = soup.find_all("a", class_="pg")

        for page in pages:

            if page.get("aria-label") == "Next Page":
                if page is not None:

                    pg_num = page.get_text()
                    pg_link = page.get("href")
                    if pg_link is not None:

                        # get page number two
                        # print("pg_num", pg_num, "page link", pg_link)
                        if "http" not in pg_link:
                            url = "https://www.jumia.co.ke/"
                            pg_link = url+pg_link

                        url = pg_link
                        page = requests.get(url, timeout=20)
                        soup = BeautifulSoup(page.content, "html.parser")
                        if soup is not None:
                            sub_category4_data = soup.find_all(
                                "a", class_="core")
                            if sub_category4_data is not None:

                                for data in sub_category4_data:
                                    # print("data available", data.prettify())
                                    image = data.find("img", class_="img")

                                    img_link = image["data-src"]
                                    product_name = data.find(
                                        "h3", class_="name").get_text()
                                    product_price = data.find(
                                        "div", class_="prc").get_text()
                                    product_discount = data.find(
                                        "div", class_="_dsct")
                                    if product_discount is not None:
                                        product_discount = product_discount.get_text()

                                    # print("product discount", product_discount)

                                    text = data.get_text()
                                    link = data.get("href")
                                    if link is not None:
                                        product_prices.append(product_price)
                                        product_discounts.append(
                                            product_discount)
                                        products_names.append(product_name)
                                        product_images.append(img_link)


# print("sub categories", sub_category_data)
df = pd.DataFrame({'product_name': products_names,
                  'product_price': product_prices,
                  "product_discount": product_discounts,
                  "product_image": product_images
                  })
print(df.to_csv("pract7.csv"))
# print("product names",len(products_names), products_names)
# print("product prices",len(product_prices), product_prices)
