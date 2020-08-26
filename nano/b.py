import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=751013"
res = requests.get(url)
res.raise_for_status() # 에러체크

soup = BeautifulSoup(res.text,"lxml")

# cartoons = soup.find_all("td",attrs={"class":"title"})

# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# 만화제목 + 링크가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title,link)

# 평점구하기
cartoons = soup.find_all("div", attrs={"class":"rating_type"})

total=0
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total += float(rate)
print("전체점수 :", total)
print("평균점수 :", total/len(cartoons))