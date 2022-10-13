import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/article/001/0013495130?cds=news_media_pc&type=editn'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, link Gecko Chrome/92.0.4515.131 Safari/537.36'}

result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, 'html.parser')

title = doc.select('h2.media_end_head_headline')[0].get_text()

#strip() : 앞뒤 공백을 제거해준다.
#get_text() : 태그를 제거하고, text만 추출
# - 회원가입
contents = doc.select('div#dic_area')[0].get_text().strip()

print(f'뉴스 제목: {title}')  #fstring
print('본문: {}'.format(contents))  #format
