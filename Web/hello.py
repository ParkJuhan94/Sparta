'''
import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    gu_name = gu['MSRSTE_NM']
    print(gu_name)
'''

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
#old_content > table > tbody > tr:nth-child(2) >
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td.point
trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    img_tag = tr.select_one('td > img')
    a_tag = tr.select_one('td.title > div > a')
    rank_tag = tr.select_one('td.point')

    if a_tag is not None:
        title = a_tag.text
        img = img_tag['alt']
        rank = rank_tag.text

        print(img, title, rank)

# C:\Users\1004s\OneDrive\Desktop\sparta\pythonprac\venv\Scripts\python.exe C:/Users/1004s/OneDrive/Desktop/sparta/pythonprac/hello.py
# 01 그린 북 9.60
# 02 가버나움 9.59
# 03 베일리 어게인 9.52
# 04 주전장 9.52
# 05 포드 V 페라리 9.51
# 06 아일라 9.49
# 07 원더 9.49
# 08 당갈 9.47
# 09 쇼생크 탈출 9.44
# 010 터미네이터 2:오리지널 9.43
# 11 보헤미안 랩소디 9.42
# 12 덕구 9.41
# 13 나 홀로 집에 9.41
# 14 월-E 9.41
# 15 살인의 추억 9.40
# 16 빽 투 더 퓨쳐 9.40
# 17 인생은 아름다워 9.39
# 18 매트릭스 9.39
# 19 라이언 일병 구하기 9.39
# 20 사운드 오브 뮤직 9.39
# 21 헬프 9.39
# 22 포레스트 검프 9.39
# 23 안녕 베일리 9.39
# 24 글래디에이터 9.39
# 25 위대한 쇼맨 9.38
# 26 센과 치히로의 행방불명 9.38
# 27 토이 스토리 3 9.38
# 28 어벤져스: 엔드게임 9.38
# 29 클래식 9.38
# 30 알라딘 9.38
# 31 헌터 킬러 9.37
# 32 죽은 시인의 사회 9.37
# 33 아이 캔 스피크 9.37
# 34 레옹 9.37
# 35 동주 9.37
# 36 반지의 제왕: 왕의 귀환 9.37
# 37 타이타닉 9.36
# 38 캐스트 어웨이 9.36
# 39 여인의 향기 9.36
# 40 집으로... 9.36
# 41 굿바이 마이 프랜드 9.35
# 42 서유기 2 - 선리기연 9.35
# 43 주토피아 9.35
# 44 두 교황 9.35
# 45 굿 윌 헌팅 9.35
# 46 클레멘타인 9.35
# 47 히든 피겨스 9.35
# 48 세 얼간이 9.35
# 49 쉰들러 리스트 9.34
# 50 울지마 톤즈 9.34

# Process finished with exit code 0
