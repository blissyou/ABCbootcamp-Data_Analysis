from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import time
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
# 크롬 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')  # 보안 기능인 샌드박스 비활성화
options.add_argument('--disable-dev-shm-usage')  # Dev/shm 디렉토리 사용 안함

service = ChromeService(executable_path=ChromeDriverManager(driver_version='127.0.6533.73').install())
driver = webdriver.Chrome(service=service, options=options)
url = 'https://www.k-apt.go.kr/bid/bidDetail.do?searchBidGb=bid_gb_1&bidTitle=%EC%88%98%EC%8B%A0%EA%B8%B0&aptName=&searchDateGb=reg&dateStart=2023-01-01&dateEnd=2023-12-31&dateArea=4&bidState=&codeAuth=&codeWay=&codeAuthSub=&codeSucWay=&codeClassifyType1=&codeClassifyType2=&codeClassifyType3=&pageNo=1&type=3&bidArea=11%7C26%7C28%7C29%7C30%7C31%7C36%7C41%7C43%7C44%7C46%7C48%7C50&bidNum=20231227170557498&bidNo=&dTime=1721830636549&mainKaptCode=&aptCode='
driver.get(url)
time.sleep(5)  # 페이지 로드 대기

# BeautifulSoup로 페이지 소스 가져오기
soup = BeautifulSoup(driver.page_source,'html.parser')
# 원하는 정보 추출
data = []
# 테이블 contTbl
table = soup.find_all('table', {'class': 'contTbl'})
# 테이블 contTbl txtC
table2 = soup.find_all('table', {'class': 'contTbl txtC'})
# print(table)

# 1 응찰회사 , 8응찰 금액, 9 낙찰여브
# company: 응찰회사 Amount:응찰금액 status: 낙찰여부
company_num =1
amount_num = 8
status_num = 9
num = 11
company =[]
amount = []
status = []
table2=table2[0].find_all('td')
print(len(table2))
# 응찰회사 응찰 금액 낙찰여부
for i in range(len(table2)):
    if company_num > len(table2) - 1:
        break
    company.append(table2[company_num].text.replace('\n','').replace('\t','').replace('\t',''))
    amount.append(table2[amount_num].text.replace('\n','').replace('\t','').replace('\t',''))
    status.append(table2[status_num].text.replace('\n','').replace('\t','').replace('\t',''))
    company_num = company_num+num
    amount_num = amount_num+num
    status_num = status_num+num

print(company)
print(amount)
print(status)

print(company)
# company = table2
# amount =
# status =
# office: 관리사무소 Group: 단체명 gen: 세대수 데이터
office = table[2].find_all('tr')[1].find_all('td')[1].text.replace('\n', '').replace('\t', '').replace('\r', '') #관리사무소
Group = table[2].find_all('tr')[1].find_all('td')[0].text.replace('\n', '').replace('\t', '').replace('\r', '') #단체명
gen = table[2].find_all('tr')[1].find_all('td')[5].text.replace('\n', '').replace('\t', '').replace('\r', '') #세대수


# d_days :마감날짜 , how: 낙찰방법
d_days = table[3].find_all('tr')[1].find_all('td')[1].text.replace('\n', '').replace('\t', '').replace('\r', '') # 마감날짜
how = table[3].find_all('tr')[3].find_all('td')[1].text.replace('\n', '').replace('\t', '').replace('\r', '') # 낙찰방법

print(office)
print(Group)
print(gen)
print(d_days)
print(how)

driver.quit()

# DataFrame으로 변환
df = pd.DataFrame(data)

# 엑셀로 저장
df.to_excel('bid_info.xlsx', index=False)
print("Data has been saved to bid_info.xlsx")
