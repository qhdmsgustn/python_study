import requests
import re
import time
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

for i in range(1,6):
    # print("페이지 :",i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

    res = requests.get(url,headers=headers)
    res.raise_for_status() # 에러체크
    soup = BeautifulSoup(res.text,"lxml")

    items = soup.find_all("li",attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div",attrs={"class":"name"}).get_text())

    for item in items:

        #광고 제품은 제외
        ad_badge = item.find("span",attrs={"class":"ad-badge-text"})

        if ad_badge:
            #print("<광고 상품 제외>")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text() # 제품명

        # 애플제품 제외
        if "Apple" in name:
            #print("<애플 상품 제외>")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text() #제품가격
        
        # 리뷰 100개 이상, 평점 4.5 이상 되는것만 조회

        
        rate = item.find("em",attrs={"class":"rating"}) #평점
        if rate:
            rate = rate.get_text()
            #print("<평점 없는 상품 제외합니다.>")
            continue
        
        rates = item.find("span",attrs={"class":"rating-total-count"})#평점수
        if rates:
            rates = rates.get_text()[1:-1]
        else:
            #print("<평점수 없는 상품 제외합니다.>")
            continue

        link= item.find("a",attrs={"class":"search-product-link"})["href"]
        
        if float(rate) >= 4.5 and int(rates) >= 100:
            # print(name,"/",price,"원 /",rate,"점 /",rates)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rates}개)")
            print("바로가기 : {}".format("https://www.coupang.com"+link))
            print("-"*50)
    time.sleep(0.5)
