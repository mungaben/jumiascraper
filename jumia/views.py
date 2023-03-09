from django.shortcuts import render


from django.http import HttpResponse, FileResponse
import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv

# scrape jumia products from jumia website 
# scrape kilimall products from kilimall website
#compare the two
#get product difference 


def Homeview(request):

    return render(request, 'jumia/home.html')
  
def Downloadproducts(requests):
    
    return render(requests, 'jumia/products.html')

def getcategories(request):
    
    return render(requests, 'jumia/categories.html')


def getsubcategories(request):
      
     
    
    return render(requests, 'jumia/subcategories.html')

def download(request):

    # url = "https://www.jumia.co.ke/"

    # page = requests.get(url)
    # # print(page.text)
    # soup = BeautifulSoup(page.content, "html.parser")
    # # print(soup.prettify())
    # # only get the text of the first paragraph
    # # get chorus class p
    # # soup.find_all('p', class_='chorus')
    # # find by id
    # # soup.find_all(id='third')
    # categ = soup.find_all("a", class_='itm')
    # # categ.decompose()
    # f = csv.writer(open('categorys.csv', 'w', newline='', encoding='UTF8'))
    # fp = csv.writer(open('product.csv', 'w', newline='', encoding="UTF8"))
    # fp2 = csv.writer(open('subcategories.csv', 'w',
    #                       newline='', encoding="UTF8"))
    # fp3 = csv.writer(open('proproduct.csv', 'w',
    #                       newline='', encoding="UTF8"))
    # # fp4=csv.writer(open('product.csv', 'w',newline='',encoding="UTF8"))
    # all_links = []
    # all_categories = []
    # subcategory_all_links = []

    # f.writerow(["category name", "category_link"])
    # fp2.writerow(["subcategory name", "subcategory_link"])
    # fp3.writerow(["primary_sub_category", "primary_subcategory_link"])

    # for a in soup.find_all('a', class_='itm'):
    #     all_links.append(a.get('href'))

    #     href = a.get('href')

    #     if href is not None:
    #         if "http" in href:
    #             print("not http")
    #             categories = a.get_text()
    #             links = a.get('href')
    #         # links = "http://www.jumia.co.ke" + a.get('href')

    #             f.writerow([categories, links])
    #             # f.writerow([links])
    #         else:
    #             links = "https://www.jumia.co.ke" + a.get('href')
    #             categories = a.get_text()
    #             f.writerow([categories, links])
    #         # all_links.append(links)

    #         # health and beauty
    #         # https://www.jumia.co.ke/health-beauty/

    #         category_url = links
    #         print("category_url", category_url)

    #         # if category_url == "https://www.jumia.co.ke/mlp-food-fest/":

    #         # f.writerow([category_url])

    #         category_page = requests.get(category_url, timeout=100)
    #         soup = BeautifulSoup(category_page.content, "html.parser")
    #         all_beautylinks = []
    #         if soup is not None and category_url != "https://www.jumia.co.ke/mlp-food-fest/" and category_url.endswith("/"):
    #             category_links = soup.find(
    #                 "div", class_=["card", "-fh"]).find_all("a", class_=["-hov-bg-gy05"])
    #             print("beauty_links", category_links)

    #             if category_links is not None:
    #                 for b in category_links:
    #                     print("beauty_links", b.get_text())
    #                     # subcategory links and data
    #                     # fp2.writerow([b.get_text(),b.get('href')])
    #                     print("beauty_links", b.get('href'))
    #                     if b.get('href') is not None:
    #                         if "http" not in b.get('href'):
    #                             b_beauty_link = "https://www.jumia.co.ke" + \
    #                                 b.get('href')
    #                             all_beautylinks.append(b_beauty_link)
    #                             fp2.writerow([b.get_text(), b_beauty_link])

    #                         else:
    #                             b_beauty_link = b.get('href')
    #                             all_beautylinks.append(b_beauty_link)
    #                             fp2.writerow([b.get_text(), b_beauty_link])

    #     #    #   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #     #                   #   getsubcategories links and names
    #                         subcategory_url = b_beauty_link
    #                         print("subcategory_url", subcategory_url)
    #                         subcategory_page = requests.get(
    #                             subcategory_url, timeout=100)
    #                         soup2 = BeautifulSoup(
    #                             subcategory_page.content, "html.parser")
    #                         all_sublinks = []

    #                         if soup2 is not None and subcategory_url != "https://www.jumia.co.ke/mlp-food-fest/":
    #                             subcategory_links = soup.find(
    #                                 "div", class_=["card", "-fh"]).find_all("a", class_=["-hov-bg-gy05"])
    #                             print("subcategory_links",
    #                                   subcategory_links)
    #                             if subcategory_links is not None:
    #                                 for b in subcategory_links:
    #                                     print(
    #                                         "subcategory_links_text", b.get_text())

    #                                     print("subcategory_links_href",
    #                                           b.get('href'))
    #                                     if b.get('href') is not None:
    #                                         if "http" not in b.get('href'):
    #                                             b_beauty_link = "https://www.jumia.co.ke" + \
    #                                                 b.get('href')
    #                                             all_beautylinks.append(
    #                                                 b_beauty_link)
    #                                             subcategory_all_links.append(
    #                                                 b_beauty_link)
    #                                             # f.writerow([b_beauty_link])
    #                                             f.writerow(
    #                                                 [b.get_text(), b_beauty_link])
    #                                         else:
    #                                             b_beauty_link = b.get(
    #                                                 'href')
    #                                             all_beautylinks.append(
    #                                                 b_beauty_link)
    #                                             subcategory_all_links.append(
    #                                                 b_beauty_link)
    #                                             f.writerow(
    #                                                 [b.get_text(), b_beauty_link])
    #                                 print("all subcategories links",
    #                                       subcategory_all_links)

    #                 # sub category products
    #     # for link in subcategory_all_links:
    #     #     product_url = link
    #     #     request = requests.get(product_url, timeout=100)
    #     #     soup3 = BeautifulSoup(request.content, "html.parser")
    #     #     SUBLINK = soup3.find_all("a", class_="core")
    #     #     for x in SUBLINK:
    #     #         xp = x.find("h3", class_="name")
    #     #         # print("product name", xp)
    #     #         if xp is not None:
    #     #         #    print("product name", xp.get_text())
    #     #            fp.writerow([xp.get_text()])
    #     #         print(x.prettify())

    #     # print("link", SUBLINK.prettify())

    #     # for x in all_links:
    #     #     print(x)
    #     #     f.writerow(links)

    #     # health and beauty
    #     # beauty_url="https://www.jumia.co.ke/health-beauty/"
    #     # beauty_page=requests.get(beauty_url)
    #     # soup = BeautifulSoup(beauty_page.content, "html.parser")
    #     # all_beautylinks=[]
    #     # beauty_links=soup.find("div",class_=["card","-fh"]).find_all("a", class_=["-hov-bg-gy05"])
    #     # print("beauty_links",beauty_links)
    #     # for b in beauty_links:
    #     #      print("beauty_links",b.get_text())
    #     #      f.writerow([b.get_text()])
    #     #      print("beauty_links",b.get('href'))
    #     #      if b.get('href') is not None:
    #     #          if "http" not in b.get('href'):
    #     #              b_beauty_link = "http://www.jumia.co.ke" + b.get('href')
    #     #              all_beautylinks.append(b_beauty_link)
    #     #              f.writerow([b_beauty_link])
    #     #          else:
    #     #              b_beauty_link =  b.get('href')
    #     #              all_beautylinks.append(b_beauty_link)
    #     #              f.writerow([b_beauty_link])

    #     # categories = soup.find_all("span", class_='text')
    #     # for p in categories:
    #     #     all_categories.append(p.get_text())
    #     #     categories = p.get_text()
    #     #     f.writerow([categories])

    #     #     print(p.prettify())

    #     # print("all categories", all_categories)
    #     # print("all links", all_links)
    #     # print("all beauty links", all_beautylinks)
    #     #

    #     # Create your views here.
    #     # file=FileResponse(f,as_attachment=True,filename="categorys.csv")
        
    return FileResponse(open("categorys.csv","rb"), as_attachment=True, filename="categorys.csv")
