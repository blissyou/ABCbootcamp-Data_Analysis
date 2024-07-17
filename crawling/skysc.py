import time
import warnings
from datetime import datetime, timedelta

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

warnings.filterwarnings('ignore')

# 날짜 데이터 생성
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


def create_driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


driver = create_driver()
time_lists = []
airport_lists = []
price_lists = []

# https://flight.naver.com/flights/international/SEL-FUK-20240713?adult=1&fareType=Y
current_month = None


def save_data():
    if time_lists and airport_lists and price_lists:
        data = pd.DataFrame({'날짜시간': time_lists, '항공사': airport_lists, '가격': price_lists})
        data.to_csv(f'flight_도쿄.csv', index=False, encoding='utf-8-sig')


for i in date:
    print(f'{i}년도 추출 추출중...{5}초 대기 예정')
    new_url = 'https://flight.naver.com/flights/international/SEL-TYO-' + i + '?adult=1&fareType=Y'
    print(new_url)

    try:
        driver.get(new_url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'route_time__xWu7a')))
    except Exception as e:
        print(e)
        driver.quit()
        driver = create_driver()
        continue

    try:
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        driver.execute_script('window.scrollTo(0, 800);')



        times = driver.find_elements(By.CLASS_NAME, 'route_time__xWu7a')[:10]
        airports = driver.find_elements(By.CLASS_NAME, 'airline_name__0Tw5w')[:10]
        prices = driver.find_elements(By.CLASS_NAME, 'item_num__aKbk4')[:10]


        year_date = str(datetime.strptime(i, '%Y%m%d'))

        for time_d in times:
            time_lists.append(year_date + '-' + time_d.text)
            print(time_d.text)

        for airport_d in airports:
            airport_lists.append(airport_d.text)
            print(airport_d.text)

        for price_d in prices:
            price_lists.append(price_d.text)
            print(price_d.text)

    except Exception as e:
        print(e)
        continue

save_data()
driver.quit()
