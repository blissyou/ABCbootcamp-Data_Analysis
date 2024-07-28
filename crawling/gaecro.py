from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request

import time
import os
import warnings
warnings.filterwarnings('ignore')

years_list= ['2019', '2020', '2021','2022','2023']
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')  # 보안 기능인 샌드박스 비활성화
options.add_argument('--disable-dev-shm-usage')  # Dev/shm 디렉토리 사용 안함

service = ChromeService(ChromeDriverManager(driver_version='127.0.6533.73').install())
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(800, 800)

soup = BeautifulSoup(driver.page_source, 'html.parser')
url = 'https://www.k-apt.go.kr/bid/bidList.do?searchBidGb=bid_gb_1&bidTitle=%EC%88%98%EC%8B%A0%EA%B8%B0&aptName=&searchDateGb=reg&dateStart=2019-01-01&dateEnd=2019-12-31&dateArea=4&bidState=&codeAuth=&codeWay=&codeAuthSub=&codeSucWay=&codeClassifyType1=&codeClassifyType2=&codeClassifyType3=&pageNo=1&type=3&bidArea=11%7C26%7C28%7C29%7C30%7C31%7C36%7C41%7C43%7C44%7C46%7C48%7C50&bidNum=&bidNo=&dTime=1721813433531&mainKaptCode=&aptCode='  # 크롤링할 웹 페이지 URL

driver.get(url)
time.sleep(3)  # 페이지 로드 대기
# 표 데이터 추출
table = soup.find('table')  # 첫 번째 테이블 찾기
rows = table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    if len(cols) > 0:
        status = cols[5].text.strip()  # 상태 컬럼 (예: 낙찰)
        amount = cols[6].text.strip().replace(',', '')  # 낙찰금액 컬럼, 콤마 제거

        if status == '낙찰' and int(amount) > 1000:
            link = row.find('a')['href']  # 행에서 링크 추출
            driver.find_element(By.XPATH, f"//a[@href='{link}']").click()  # 링크 클릭
            time.sleep(2)  # 클릭 후 페이지 로드 대기

            # 필요한 작업 수행 (예: 세부 정보 추출 등)
            detail_page_soup = BeautifulSoup(driver.page_source, 'html.parser')
            # 세부 정보 추출 코드 추가
            # ...

            driver.back()  # 원래 페이지로 돌아가기
            time.sleep(2)

driver.quit()
# for i in years_list:
#     new_url = f'https://www.k-apt.go.kr/bid/bidList.do?searchBidGb=bid_gb_1&bidTitle=%EC%88%98%EC%8B%A0%EA%B8%B0&aptName=&searchDateGb=reg&dateStart={i}-01-01&dateEnd={i}-12-31&dateArea=4&bidState=&codeAuth=&codeWay=&codeAuthSub=&codeSucWay=&codeClassifyType1=&codeClassifyType2=&codeClassifyType3=&pageNo=1&type=3&bidArea=11%7C26%7C28%7C29%7C30%7C31%7C36%7C41%7C43%7C44%7C46%7C48%7C50&bidNum=&bidNo=&dTime=1721813433531&mainKaptCode=&aptCode='
#     driver.get(new_url)
#     if i == '2019':
#         for j in range(1, 26):
#
#     elif i == '2020':
#         for j in range(1, 25):
#             print(j)
#     elif i == '2021':
#         for j in range(1, 28):
#             print(j)
#     elif i == '2022':
#         for j in range(1, 28):
#             print(j)
#     elif i == '2023':
#         for j in range(1, 28):
#             print(j)
