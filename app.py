import requests
from bs4 import BeautifulSoup

# 함수 - 화장품 이름, 가격, 링크주소
def get_product_info(box):
    ptag = box.find("p", {"class": "name"})
    spans_name = ptag.findAll("span")
    ul = box.find("ul")
    span_price = ul.findAll("span")

    name = spans_name[1].text
    price = span_price[1].text

    atag = box.find("a")
    link = atag["href"]

    return {"name": name, "price": price, "link": link}


# 함수 - 페이지 데이터 가져오기
def get_page_products(url, headers):
    result = requests.get(url, headers=headers)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    ul = bs_obj.find("ul", {"class": "prdList column5"})

    boxes = ul.findAll("div", {"class": "box"})
    product_info_list = [get_product_info(box) for box in boxes]

    return product_info_list


urls = [
    "http://jolse.com/category/tonermist/43/?page=1",
    "http://jolse.com/category/tonermist/43/?page=2",
    "http://jolse.com/category/tonermist/43/?page=3",
    "http://jolse.com/category/tonermist/43/?page=4",
    "http://jolse.com/category/tonermist/43/?page=5",
]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}

for page_number in range(0, 5):
    page_products = get_page_products(urls[page_number], headers)
    print(len(page_products), page_products)

