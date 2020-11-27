import pricetoint as pti
import requests
from bs4 import BeautifulSoup

#1 당근마켓 Search = Keyword(입력) 받아 웹 크롤링(가격부분)
keyword="바운서"
market_result = requests.get("https://www.daangn.com/search/"+keyword)
market_soup=BeautifulSoup(market_result.text,"html.parser")
section_result=market_soup.find_all("article",{"class":"flea-market-article flat-card"})

#2 크롤링한 Str 형태의 가격들을 리스트에 저장 (공백포함)
price_all=[]
count=0
for price in section_result:
    price_result=price.find("p",{"class":"article-price"})
    price_all.insert(count,str(price_result.string))
    count+=1

#3 크롤링한 Str 형태의 가격들을 리스트에 저장 (공백제거)
count=0
price_result=[]
for i in price_all:
    price_result.insert(count,i.strip())
    count+=1

#4 크롤링한 Str 형태의 가격들을 int 형태로 변환하고 평균값 계산
# 각각의 가격들은 price_result list에 str형태로 저장
sum_all=0
price_middle=0
for i in price_result :
    if i=="무료나눔" : continue #무료나눔은 0원으로 계산
    else :
        a=pti.price_to_int(i)
        sum_all+=a
        # int 형태로 변환된 가격 출력
        #print(a)

price_middle=sum_all/count
print(int(price_middle))