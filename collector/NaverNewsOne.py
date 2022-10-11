import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/article/001/0013495130?cds=news_media_pc&type=editn'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, link Gecko Chrome/92.0.4515.131 Safari/537.36'}

result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, 'html.parser')

title = doc.select('h2.media_end_head_headline')[0].get_text()

contents = doc.select('section p')

print(f'뉴스 제목: {title}')

content = ''
for line in contents:
    content += line.get_text()
print(f'뉴스본문: {content}')