

import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv


# get product names
# from categories>subcategories>sub2categories>sub3category>sub4category>products
#       home supermarket >food cupboard>cooking ingridient2>condiments3>hotsouse4>product generic intense


# csv to write data  category name,category link
fp = csv.writer(open('maincategory.csv', 'w', newline='',
                encoding="utf_8"), delimiter=",")
# home url of jumia

url = "https://www.jumia.co.ke/"


page = requests.get(url, timeout=20)
# homepage html tree
soup = BeautifulSoup(page.content, "html.parser")
# home main categories
categ = soup.find_all("a", role="menuitem", class_='itm')
# write colums
fp.writerow(["category name", "category link"])

# read written csv

# print(df)
main_category_names = []
main_category_links = []

for i in categ:
    print(i.prettify())
    if i is not None:
        text = i.get_text()
        print("category name", text)

    if text is not None:
        link = i.get("href")
        print("category link", link)
        if link is not None:
            main_category_names.append(text)
            if "http" not in link:
                main_category_links.append(url+link)
            else:
                main_category_links.append(link)


df = pd.DataFrame({"category name": main_category_names,
                  "category link": main_category_links})
print(df)


# subcategories
subcategory_names = []
subcategory_links = []
for link in main_category_links:
    url = link
    page = requests.get(url, timeout=20)
    soup = BeautifulSoup(page.content, "html.parser")
    if soup is not None:
        sub_category = soup.find(
            "div", class_=["card", "-fh"]).find_all("a", class_=["-hov-bg-gy05"])
        if sub_category is not None:
            for data in sub_category:
                text = data.get_text()
                link = data.get("href")
                if link is not None:
                    subcategory_names.append(text)
                    if "http" not in link:
                        url = "https://www.jumia.co.ke/"
                        subcategory_links.append(url+link)
                    else:
                        subcategory_links.append(link)
df = pd.DataFrame({"category name": subcategory_names,
                  "category link": subcategory_links})
print(df)


#  subcategory2
subcategory2_names = []
subcategory2_links = []
for link in subcategory_links:
    url = link
    page = requests.get(url, timeout=20)
    soup = BeautifulSoup(page.content, "html.parser")
    if soup is not None:
        sub_category2 = soup.find(
            "div", class_=["card", "-fh"]).find_all("a", class_=["-hov-bg-gy05"])
    if data is not None:
        for data in sub_category2:
            text = data.get_text()
            link = data.get("href")
            if link is not None:
                subcategory2_names.append(text)
                if "http" not in link:
                    url = "https://www.jumia.co.ke/"
                    subcategory2_links.append(url+link)
                else:
                    subcategory2_links.append(link)

df = pd.DataFrame({"category name": subcategory2_names,
                  "category link": subcategory2_links})
print(df)

# get subcategories3 about 20min
# CATEGORY
# Team Sports
# Soccer
# Accessories
# Balls
# Clothing
# Footwear
# Player Equipment
# Training Equipment
sub_category3_names = []
sub_category3_links = []

for link in subcategory2_links:
    url = link
    page = requests.get(url, timeout=100)
    soup = BeautifulSoup(page.content, "html.parser")
    if soup is not None:
        sub_category3_data = soup.find_all(
            "a", class_="-phxl")
        if sub_category3_data is not None:
            for data in sub_category3_data:
                text = data.get_text()
                link = data.get("href")
                if link is not None:
                    sub_category3_names.append(text)
                    if "http" not in link:
                        url = "https://www.jumia.co.ke/"
                        sub_category3_links.append(url+link)
                    else:
                        sub_category3_links.append(link)


df = pd.DataFrame({"category name": sub_category3_names,
                  "category link": sub_category3_links})
print(df)


#  subcategory4
# CATEGORY
# Team Sports
# Soccer   (subcategory4)
# Accessories
# Balls
# Clothing
# Footwear
# Player Equipment
# Training Equipment

sub_category4_names = []
sub_category4_links = []
for link in sub_category3_links:
    url = link
    page = requests.get(url, timeout=100)
    soup = BeautifulSoup(page.content, "html.parser")
    if soup is not None:
        sub_category4_data = soup.find_all("a", class_="-phxl")
        if sub_category4_data is not None:
            for data in sub_category4_data:
                text = data.get_text()
                link = data.get("href")
                if link is not None:
                    sub_category4_names.append(text)
                    if "http" not in link:
                        url = "https://www.jumia.co.ke/"
                        sub_category4_links.append(url+link)
                    else:
                        sub_category4_links.append(link)

df = pd.DataFrame({"category name": sub_category4_names,
                  "category link": sub_category4_links})
print(df)

# products
# CATEGORY
#   Soccer
# Accessories
# Equipment Bags
# Field Accessories

products_names = []
product_images = []
product_prices = []
product_discounts = []
for link in sub_category4_links:
    url = link
    page = requests.get(url, timeout=100)
    soup = BeautifulSoup(page.content, "html.parser")
    if soup is not None:
        sub_category4_data = soup.find_all("a", class_="core")
        for data in sub_category4_data:
            image = data.find("img", class_="img")
            img_link = image["data-src"]
            product_name = data.find("h3", class_="name").get_text()
            product_price = data.find("div", class_="prc").get_text()

            product_discount = data.find("div", class_="_dsct")

            if product_discount is not None:
                product_discount = product_discount.get_text()
            print("product discount", product_discount)
            if product_name is not None:
                products_names.append(product_name)
                product_discount.append(product_discount)
                product_images.append(img_link)
                product_prices.append(product_price)
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



df = pd.DataFrame({"product name": products_names, "product link": product_images,
                  "product price": product_prices, "product discount": product_discounts})
df.to_csv("productsdata.csv")
print(df)

print("number of categories", len(categ))
