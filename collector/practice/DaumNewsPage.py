import requests
from bs4 import BeautifulSoup
from collector.practice.CollectorService import get_daum_news

# 1페이지에서 15개의 뉴스(제목, 본문) 수집 코드
# 1 ~ 끝 페이지 돌면서 수집 수정

# range(시작값, 끝값, 크기)
#  - 크기는 생략 가능(default 1)
# - 끝값은 -1까지로 생각
# -> range(1, 3, 1) = [1, 2]
# -> range(1, 10, 2) = [1, 3, 5, 7, 9]
news_count = 0
num = 0
while True:
    num += 1
    print(f'▶ page {num}')
    url = f'https://news.daum.net/breakingnews/digital?page={num}'  # 1 page
    result = requests.get(url)

    # 'https://news.daum.net/breakingnews/digital?page=8'
    # 쿼리스트링(QueryString): url(주소) + data
    # utl ? data
    doc = BeautifulSoup(result.text, 'html.parser')
    title_list = doc.select('ul.list_news2 a.link_txt')

    if title_list == None :
        break

    for i, title in enumerate(title_list):
        print(f'index: {i + 1}, url: {title["href"]}')
        get_daum_news(title["href"])
        print("\n")
        news_count += 1

print(f'총 {news_count}개의 뉴스를 수집하였습니다.')
