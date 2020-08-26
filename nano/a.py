import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() # 에러체크

soup = BeautifulSoup(res.text,"lxml")

# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs)
# a = soup.find("a",attrs={"class":"Nbtn_upload"})
# a = soup.find(attrs={"class":"Nbtn_upload"})
# print(a)

# print(soup.find("li",attrs={"class":"rank01"}))
# rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank1.parent())
# print(rank1.a.get_text())
# rank2=rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3=rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank4=rank3.find_next_sibling("li")
# print(rank4.a.get_text())
# rank2 = rank1.find_next_siblings("li")

webtoon = soup.find("a",text = "고수-2부 111화")
print(webtoon.a.get_text())