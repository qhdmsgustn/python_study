from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.maximize_window() # 창 최대화

#이동
url = "https://flight.naver.com/flights/"
browser.get(url)

#가는날 선택
browser.find_element_by_link_text("가는날 선택").click()


#이번달 29 이번달 31
# browser.find_elements_by_link_text("30")[0].click() #[0]>이번달
# browser.find_elements_by_link_text("31")[0].click()

#이번달 30 다음달 5
browser.find_elements_by_link_text("30")[0].click() #[0]>이번달
browser.find_elements_by_link_text("5")[1].click()

#제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색
browser.find_element_by_link_text("항공권 검색").click()

#조건값이 나올떄까지 기다려보기[로딩!]
try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    #기다린 후 동작
    print(elem.text)

finally:
    print("종료")
    browser.quit()


