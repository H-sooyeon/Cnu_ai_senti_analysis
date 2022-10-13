import requests
from bs4 import BeautifulSoup
import pprint

url = 'https://news.daum.net/breakingnews/digital'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')

title_list = doc.select('ul.list_news2 a.link_txt')

#pprint.pprint(title_list)
#print(len(title_list))

# <a href="url"> : a태그는 클릭했을 때 해당 url로 이동
#len(): list[]의 갯수를 알려주는 함수

# enumerate() : index 번호와 itme을 반복을 돌며 가져온다.
# list[]의 index는 0번부터 시작
#len(list) = 15, index = 0~14
for i, title in enumerate(title_list):
    print(f'index: {i}, url: {title.get_text()}')
