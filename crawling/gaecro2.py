from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
years_list= ['2019', '2020', '2021','2022','2023']
# Selenium 설정
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')  # 보안 기능인 샌드박스 비활성화
options.add_argument('--disable-dev-shm-usage')  # Dev/shm 디렉토리 사용 안함

service = ChromeService(ChromeDriverManager(driver_version='127.0.6533.73').install())
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(800, 800)

soup = BeautifulSoup(driver.page_source, 'html.parser')
for i in years_list:
    new_url = f'https://www.k-apt.go.kr/bid/bidList.do?searchBidGb=bid_gb_1&bidTitle=%EC%88%98%EC%8B%A0%EA%B8%B0&aptName=&searchDateGb=reg&dateStart={i}-01-01&dateEnd={i}-12-31&dateArea=4&bidState=&codeAuth=&codeWay=&codeAuthSub=&codeSucWay=&codeClassifyType1=&codeClassifyType2=&codeClassifyType3=&pageNo=1&type=3&bidArea=11%7C26%7C28%7C29%7C30%7C31%7C36%7C41%7C43%7C44%7C46%7C48%7C50&bidNum=&bidNo=&dTime=1721813433531&mainKaptCode=&aptCode='
    driver.get(new_url)
    time.sleep(5)
    table = soup.find('table')  # 첫 번째 테이블 찾기
    rows = table.find_all('tr')
    if i == '2019':
        
    elif i == '2020':

    elif i == '2021':

    elif i == '2022':

    elif i == '2023':



# BeautifulSoup로 페이지 소스 가져오기
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 표 데이터 추출
table = soup.find('table')  # 첫 번째 테이블 찾기
rows = table.find_all('tr')



driver.quit()
