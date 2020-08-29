# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies/top"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.22 Safari/537.36",
#     "Accept-Language":"ko-KR,ko"
#     }

# res = requests.get(url,headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,"lxml")

# movies = soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})

# for idx,movie in enumerate(movies):
#     title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
#     print(str(idx+1)+": "+title)


# with open("movie.html","w",encoding="utf-8-sig") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) #html 문서를 이쁘게

from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("windows-size=3440x1440")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.22 Safari/537.36")

browser = webdriver.Chrome(options=options)
url = "https://play.google.com/store/movies/top"
browser.get(url)

#스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)")
# browser.execute_script("window.scrollTo(0,2080)")
#지정한 위치로 스크롤 내리기

#화면 가장아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

interval = 2 #2초에 한번씩 스크롤 내림

#현재 문서 높이를 가져와서 저장
prev_height= browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(interval)

    curr_height= browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source,"lxml")
movies = soup.find_all("div",attrs={"class":["Vpfmgd"]})#리스트 일경우 and연산

for idx,movie in enumerate(movies):
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    #할인 전 가격 정보
    original_price = movie.find("span",attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title,"[할인 되지 않은 영화 제외]")
        continue
    
    #할인 된 가격
    price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    
    #링크 https://play.google.com/ + link
    link = movie.find("a",attrs={"class":"JC71ub"})["href"]
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ","https://play.google.com"+link)
    print("-"*100)

browser.quit()