import pricetoint as pti
from bs4 import BeautifulSoup
import requests #requests 사용
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime

#1 당근마켓 Search = Keyword(입력) 받아 웹 크롤링(가격부분)
keyword="플레이스테이션4" # 사용자에게 입력받아야하는 변수

## requests사용
"""
market_result = requests.get("https://www.daangn.com/search/"+keyword)
market_soup=BeautifulSoup(market_result.text,"html.parser")
section_result=market_soup.find_all("article",{"class":"flea-market-article flat-card"})
"""

## Selenium 사용
driver = webdriver.Chrome('./driver/chromedriver')
driver.implicitly_wait(1)
driver.get("https://www.daangn.com/search/"+keyword)

#더보기 버튼 2번클릭
button = driver.find_element_by_xpath('//*[@id="result"]/div[1]/div[2]')

#당근 마켓 더보기 버튼 1번클릭마다 +12개 갱신 (기본6개)

button_count=3 # 버튼 누르는 횟수 (+12개) + 사용자에게 입력 받아야하는 변수

for i in range(0,button_count) :
    button.click()
    driver.implicitly_wait(1)


#가격부분 크롤링 (더보기 갱신한 만큼) - Selenium: Xpath 사용
price_div=[]
for i in range(1,43) :
    path_url = '//*[@id="flea-market-wrap"]/article['+str(i)+']/a/div[2]/p[2]'
    price_div.insert(i-1,driver.find_element_by_xpath(path_url).text)

#2 크롤링한 Str 형태의 가격들을 리스트에 저장 (공백포함)
"""
price_all=[]
count=0
for price in section_result:
    price_result=price.find("p",{"class":"article-price"})
    price_all.insert(count,str(price_result.string))
    count+=1
"""

"""
#3 크롤링한 Str 형태의 가격들을 리스트에 저장 (공백제거)
count=0
price_result=[]
for i in price_all:
    price_result.insert(count,i.strip())
    count+=1
"""

#4 크롤링한 Str 형태의 가격들을 int 형태로 변환하고 평균값 계산
# 각각의 가격들을 price_result list에 str형태로 저장 (requests 버전)
# 각각의 가격들을 price_div list에 str형태로 저장 (selenium 버전)
count=0
free_count=0
sum_all=0
price_middle=0
for i in price_div :
    if i=="무료나눔" :
        free_count+=1 # 무료나눔 갯수
        continue #무료나눔은 계산에서 제외
    else :
        count+=1
        a=pti.price_to_int(i)
        sum_all+=a
        # int 형태로 변환된 가격 출력
        #print(a)

price_middle=sum_all/count # 무료나눔 제외한 개수로 평균시세 도출

print(int(price_middle))