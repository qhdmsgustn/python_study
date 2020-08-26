from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./image/chromedriver.exe')
driver.implicitly_wait(2)

driver.set_window_size(2000, 1200)

driver.get('https://discord.com/channels/474739462589382667/479481126373687297')
print("1. 접속성공")

driver.find_element_by_name('email').send_keys('qhdmsgustn@naver.com')
driver.find_element_by_name('password').send_keys('gus1408411@')
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()
driver.implicitly_wait(5)
print("2. 로그인성공")

#이모지 창 클릭
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[2]/div[2]/button/div/div').click()

#이모지 창 늘리기

# 검색
driver.find_element_by_xpath('//*[@id="emoji-picker-tab-panel"]/div[1]/div[1]/div[1]/div/input').send_keys('Rok')

print("3. 창크기 수동 조절")
time.sleep(5)

print("4. 크롤링시작")
for idx,el in enumerate(driver.find_elements_by_class_name("emojiItem-14v6tW")):
    el.screenshot(str(idx)+".png")
