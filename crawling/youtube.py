from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import time
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')  # 보안 기능인 샌드박스 비활성화
options.add_argument('--disable-dev-shm-usage')  # Dev/shm 디렉토리 사용 안함

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(800, 800)

driver.get('https://www.youtube.com/watch?v=a11IohJX40A')
driver.implicitly_wait(10)  #화면 렌더링 기다리기

# 사람인척 하기
time.sleep(10)
driver.execute_script('window.scrollTo(0, 800);')
time.sleep(5)

# 댓글 수집을 위한 스크롤 내리기

last_height = driver.execute_script('return document.documentElement.scrollHeight')

while True:
    print('스크롤 중...')
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
    time.sleep(3)

    new_height = driver.execute_script('return document.documentElement.scrollHeight')
    if new_height == last_height:
        break

    last_height = new_height
    time.sleep(3)
# 댓글 크롤링
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

# 댓글 태그 리스트 가져오기
comment_list = soup.select('yt-attributed-string#content-text')
comment_final = []
print('댓글의 수', str(len(comment_list)))

# 댓글 텍스트 추출
for i in range(len(comment_list)):
    temp_comment = comment_list[i].text
    temp_comment = temp_comment.replace('\n', '').replace('\t', '').replace('\r', '').strip()
    print(temp_comment)
    comment_final.append(temp_comment) # 댓글 내용

# 데이터 프레임에 담기

youtube_dic = {'댓글내용': comment_final}
youtube_df = pd.DataFrame.from_dict(youtube_dic)

print('=='*30)
print('크롤링 종료 ...')
print('=='*30)
# 수집된 데이터 확인하기

print(youtube_df.info())
youtube_df.to_csv('유튜브댓글_크롤링_과제_20240709.csv',encoding='utf-8- sig',index=False)

print('=='*30)
print('파일 저장 완료 ...')

# 브라우저 닫기

driver.close()