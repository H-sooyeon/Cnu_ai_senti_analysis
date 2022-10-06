#주석
## -> 개발자의 메모장 > 파이썬이 주석은 실행하지 않는다.
#파이썬의 경로
#1. 프로젝트(cnu_ai_senti_analysis-m, main)
#  -> 2. python 패키지(collector)
#       -> 3. Python file(text.py, DaumNewsOne.py)
# - Python package: 파이썬 file들을 모아두는 폴더
#           폴더 아이콘 안에 구멍이 뚫려있다.
# import와 Library(module)
# - Python 코드를 직접 작성해서 개발할 수도 있지만
# - 다른 개발자가 이미 만들어 놓은 코드를 사용하면 편리함
# - 이미 개발되어 있는 코드들의 묶음 = 라이브러리(module)
# 1.built in library : Python 설치하면 자동으로 제공
#           예) math, sysm os 등
# 2.외부 Library : 여러분이 직접 추가해서 사용!
#           예) requests, beautifulsoup4

# Library를 사용하기 위해서는 import 작업 진행
# - import는 도서관에서 필요한 책을 빌려오는 개념

import requests # 책 전체를 빌려옴
from bs4 import BeautifulSoup # bs4라는 책에서 beautifulsoup 1개 파트만 빌려옴

# 목표: Daum 뉴스 웹 페이지에서 제목과 본문 데이터를 수집!
# 1.url: https://v.daum.net/v/20221006104506521
url='https://v.daum.net/v/20221006104506521'
# 2.requests로 해당 url의 html 전체 코드를 수집!

result = requests.get(url) # request 함수가 client에게서 request를 직접 얻어 server에게 전달해주고 response를 얻어옴
# print(result.text)
# client인 웹 브라우저가 server인 Daum news에게 url에 대한 소스를 요청(requests)
# server는 client는 url에 대한 소스를 제공(response) -> 200으로 표시

# 3.beautifulsoup을 통해서 '제목과 본문'만 추출
doc = BeautifulSoup(result.text, 'html.parser')
# python은 []: List Type
# index    0  1  2  3
#       - [5, 6, 7, 10] : List 내에는 다양한 데이터를 담을수 있다.
# [5]
title = doc.select('h3.tit_view')[0].getText()
print(f'뉴스 제목: {title}')