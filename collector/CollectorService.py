#########################################
# Collector 비즈니스 로직을 모아둔 파이썬 파일
#########################################
# Date: 2022.10.18: 파일 생성 : 황수연
#########################################

#함수 생성
# - 함수: 반복적으로 사용하는 기능을 코드로 묶어서 만듬
# - 사용: 함수 이름으로 호출!
# - python에서 () 붙어 있으면 대부분 함수
# - 예: print(), pprint(), get(), get_text()
# - 내장 함수: 파이썬 설치 시 기본 제공
# - 사용자 정의 함수: 직접 만들어서 사용
# - 외부 함수: 다른 개발자가 만들어 놓은 것을 import 해서 사용
#            ex) requests.get(), BeautifulSoup()
import requests
from bs4 import BeautifulSoup

# python naming rule
# 1) 파스칼(pascal)    -> GetDaumNews
# 2) 카펠(camel)      -> getDaumNews
# 3) 스네이크(snake)   -> get_daum_news
def get_daum_news(url) :
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.tit_view')[0].get_text()
    contents = doc.select('section p')

# if문 -> 제어문(조건이 true인 경우에만 실행)
# != 같지 않다.
    print(f'뉴스 제목: {title}')
    if len(contents) != 0: # 본문이 있는 경우에만
        content = ''

        for line in contents:  # 순서대로 <p>를 가져와서 line에 넣고 다음 코드 실행
            content += line.get_text()

        print(f'뉴스본문: {content}')
