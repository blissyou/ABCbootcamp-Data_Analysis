from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import warnings
import random
warnings.filterwarnings('ignore')


# BeautifulSoup 객체 생성

# 날짜 데이터 생성
from datetime import datetime, timedelta

date = []

start = "20240801"
last = "20250630"

start_date = datetime.strptime(start, "%Y%m%d")
last_date = datetime.strptime(last, "%Y%m%d")

# 종료일 까지 반복
while start_date <= last_date:
    dates = start_date.strftime("%Y%m%d")
    date.append(dates)
    start_date += timedelta(days=1)

# 보안 인스턴스 해지
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')  # 보안 기능인 샌드박스 비활성화
options.add_argument('--disable-dev-shm-usage')  # Dev/shm 디렉토리 사용 안함

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

for d in date:
    # 랜덤 초 생성
    random_sec = random.randint(1, 40)

    # 년도 url 생성
    print(f'{d}년도 추출 추출중...{random_sec}초 대기 예정')
    new_url = 'https://flight.naver.com/flights/international/SEL-FUK-' +d + '?adult=1&fareType=Y'
    print(new_url)
    time.sleep(random_sec)



    #url 열기
    driver.get(new_url)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    results = driver.find_elements(By.CLASS_NAME, 'indivisual_IndivisualItem__CVm69')
    print(results)
    for result in results:
        try:
            alirline = result.find_element(By.CLASS_NAME,'airline_name__0Tw5w').text
            prise = result.find_element(By.CLASS_NAME,'item_num__aKbk4').text
            time = result.find_element(By.CLASS_NAME, 'route_time__xWu7a').text
            print(alirline, time, prise)
        except:
            pass
