# 필요 모듈 임포트
import urllib.request

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import os

# 2. 폴더 생성

def createFolder(dirctory):
    try:
        if not os.path.exists(dirctory):
            os.makedirs(dirctory)
    except os.error:
        print("Error : creating directory.." + dirctory)

# 3. 키워드 입력 및 폴더 생성
keyword = '꽃'
createFolder('./'+keyword+'_img_download')

print('1. 키워드 폴서 생성 완료')
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')  # 보안 기능인 샌드박스 비활성화
options.add_argument('--disable-dev-shm-usage')  # Dev/shm 디렉토리 사용 안함

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

print('2. 키워드 검색:',keyword)
driver.implicitly_wait(10)

driver.get('https://www.google.co.kr/imghp?hl=ko')

# 검색창 element 찾기 / 구글 이미지 검색은 textarea name="q"
input_keyword = driver.find_element(By.NAME, 'q')
input_keyword.send_keys(keyword)
# 입력값 전송
input_keyword.send_keys(Keys.RETURN)
# 스크롤 내리기
SCROLL_PAUSE_TIME = 5

last_height = driver.execute_script('return document.body.scrollHeight')
print('3.스크롤 중...'+keyword)

while True:
    print('스크롤 중...')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break

    last_height = new_height
    time.sleep(SCROLL_PAUSE_TIME)

# 6. 이미지 검색 개수 확인 및 다운로드

links = []
images = []

# img 태그를 감싼 div 찾기 <div class="H8Rx8c">
div = driver.find_elements(By.CLASS_NAME,'H8Rx8c')

for i in div[:100]:
    img_tag = i.find_element(By.CLASS_NAME,'YQ4gaf')
    images.append(img_tag)
print("4. 이미지 개수 확인...")
for image in images:
    if image.get_attribute('src') !=None:
        links.append(image.get_attribute('src'))

print(keyword + '찾은 이미지 개수:',len(links))
time.sleep(SCROLL_PAUSE_TIME)

print("이미지 다운로드 시작...")

for i , v in enumerate(links[:100]):
    try:
        url = v
        start = time.time()
        urllib.request.urlretrieve(url, './'+keyword+'_img_download/'+keyword+'_'+str(i)+'.jpg')
        print(str(i+1)+'/'+str(len(links))+keyword+'다운로드...Download time: '+ str(time.time()-start)[:5]+'초')
    except:
        print(str(i + 1) + '/' + str(len(links)) + keyword + '다운로드 실패.... ')
        pass
print(keyword+'------다운로드 종료')
