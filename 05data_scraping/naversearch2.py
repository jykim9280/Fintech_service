import requests
import pandas as pd
import time
from dotenv import load_dotenv #ID,PW 숨겨줌
import os

#.env 파일에서 환경 변수 로드
load_dotenv()

#환경 변수에 접근

def naver_search2():
    '''
    네이버 검색 서비스를 Requests를 사용해서 구현한 모듈입니다.
    '''
    book_lists = []
    page = 1
    start = 1
    service = input("카테고리를 입력하세요(blog,book,news,doc): ").lower()
    query = input("검색어를 입력하세요: ")
    while True:
        client_id = os.getenv('client_id')
        client_secret = os.getenv('client_secret')
        url = f"https://openapi.naver.com/v1/search/{service}"
        payload = {'query' : query , 'display' : 10, 'start' : start, 'sort' : 'sim'}
        headers = {'X-Naver-Client-Id' : "VfCSVYpBxY6EEAWW1zcr", 'X-Naver-Client-Secret' : "bTXn2nJ3Ig"}
        try:
            r = requests.get(url, params = payload, headers = headers)
            print(r.url)
            print(r.status)
            if(r.status_code ==200):
                data = r.json()
                result2 = pd.json_normalize(data['items'])
                total_page = data['items'] // 10 + 1
                print(result2)
            else:
                print("Error Code:" + str(r.status_code))
                break
            if page < total_page:
                page += 1
                if start != 991:
                    start += 10
                elif start == 991:
                    start += 9
                print(f"{page:03d}/{total_page:03d}, start: {start} 추출중", end="\r")
            else:
                break
            time.sleep(0.5)
        except Exception as e:
            print(e)
            break