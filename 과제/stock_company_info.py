import time
from datetime import date
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = "https://kind.krx.co.kr/corpgeneral/corpList.do"
payload = dict(method='searchCorpList',pageIndex=1,currentPageSize=15,comAbbrv="",beginIndex="",orderMode='3',orderStat='D',isurCd="",repIsuSrtCd="",searchCodeType="",marketType="",searchType='13',industry="",fiscalYearEnd='all',comAbbrvTmp="",location='all')
r = requests.get(url, params = payload)
print(r.url)
soup = bs(r.text, 'lxml')

keys = soup.select_one("table.list.type-00.tmt30")['summary'].split(", ")

page = 1
page_size = 100
final_result_df = pd.DataFrame()
while True:
    url = "https://kind.krx.co.kr/corpgeneral/corpList.do"
    payload = dict(method='searchCorpList',pageIndex=page, currentPageSize=page_size,orderMode=3,orderStat='D',searchType=13, fiscalYearEnd='all', location='all')
    r = requests.get(url, params=payload)
    print(r.status_code, end="\r")
    soup = bs(r.text, 'lxml')
    total_items = int(soup.select_one(".info.type-00 > em").text.replace(",", ""))
    total_pages = total_items // page_size + 1
    print(f"{page}/{total_pages} 수집중", end="\r")
    keys = soup.select_one("table.list.type-00.tmt30")['summary'].split(", ")  
    result = {}
    for tr in soup.select('tr'):
        for idx, (key, td) in enumerate(zip(keys, tr.select('td'))):
            if idx == 0:
                kinds = [img['alt'].strip() for img in td.select('img')]   # 1번째 증권 종류, 회사이름
                kind = ", ".join(kinds)
                code = td.select_one("a")['onclick'].split("'")[1] # 종목코드 추출
                result.setdefault('증권종류', []).append(kind)
                result.setdefault(key, []).append(td.text)
                result.setdefault('종목코드', []).append(code+"0") # 종목코드 추가
            elif idx == 6:
                home_link = td.select_one('a')['href'] if td.string == None else ""  # 6번째 링크 찾기
                result.setdefault(key, []).append(home_link)
            else:
                result.setdefault(key, []).append(td.text)
    result_df = pd.DataFrame(result)
    final_result_df = pd.concat([final_result_df, result_df])
        
    if page < total_pages:
        page += 1
        time.sleep(5)
    else:
        break

import os
from datetime import datetime
from sqlalchemy import create_engine, text
import pymysql
pymysql.install_as_MySQLdb()

# 데이터베이스 접속 정보 설정 (환경 변수 대신 문자열을 직접 사용)
db = "mysql"
dbtype = "pymysql"
user = "root"
password = "1234"
host = "127.0.0.1:3306"
database = "korean_stock"

# MySQL 서버에 연결 (데이터베이스를 지정하지 않고 접속)
engine = create_engine(f"{db}+{dbtype}://{user}:{password}@{host}")

conn = engine.connect()

# 데이터베이스 삭제 및 생성
conn.execute(text(f"DROP DATABASE IF EXISTS {database}"))
conn.execute(text(f"CREATE DATABASE {database}"))
conn.close()

# 새로 생성한 데이터베이스로 다시 연결
engine = create_engine(f"{db}+{dbtype}://{user}:{password}@{host}/{database}")
conn = engine.connect()

# DataFrame을 MySQL 테이블로 저장 (final_result_df가 정의되어 있어야 함)
# final_result_df는 사용자가 사전에 정의한 DataFrame이어야 합니다.
final_result_df.to_sql('stock_company_info_김지연', con=conn, if_exists='append', index=False)
conn.close()
