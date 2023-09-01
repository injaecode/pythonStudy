import requests
from bs4 import BeautifulSoup

keyword = '파이썬' # 검색할 키워드

raw = requests.get('https://search.naver.com/search.naver?&where=news&query=' + keyword).text
html = BeautifulSoup(raw, 'html.parser')

articles = html.select('.list_news > li') # 뉴스 article select
for article in articles:
    title = article.select_one('div.news_area > a').text  # 제목
    url = article.select_one('div.news_area > a')['href']  # 링크URL
    print(title, url)  # 출력
