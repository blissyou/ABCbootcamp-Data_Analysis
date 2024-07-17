"""

멜론차트 시대별 차트 음악 정보 수집
https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2020

데이터 수집 순서
1. 연도 선택 -> 해당연도 페이지로 이동 -> 연간 차트 1~30위 까지 노래 제목, 가수 정보 수집 ->
2. 각 노래 가사 수집 -> 곡정보 페이지 이도 -> 노래 가사 화면의 펼치기 버튼 클릭-> 가사 수집
3.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import time
import pandas as pd
import re
from pytz import timezone
import datetime

import warnings


def melon_collector(url, start):
    warnings.filterwarnings('ignore')

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')  # 보안 기능인 샌드박스 비활성화
    options.add_argument('--disable-dev-shm-usage')  # Dev/shm 디렉토리 사용 안함

    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    print(str(start) + '년도 멜론 TOP30 수집 시작--------------')
    driver.get(url)
    time.sleep(3)

    driver.execute_script('window.scrollTo(0, 800);')
    time.sleep(3)

    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    # 노래 제목 30개 추출

    titles = driver.find_elements(By.CSS_SELECTOR, '.ellipsis.rank01')
    title_list = [title.text for title in titles][:30]
    print(title_list)
    # 가수 30개 추출
    singers = driver.find_elements(By.CSS_SELECTOR, '.ellipsis.rank02')
    singer_list = [singer.text for singer in singers][:30]
    print(singer_list)

    # 가사 수집을 위한 songid 추출
    song_info = soup.find_all('div', {'class': 'ellipsis rank01'})

    songid_list = []

    #javascript:melon.play.playSong('19070207','32313543')
    for sid in song_info[:30]:
        try:
            info = re.sub('[^0-9]', '', sid.find('a')['href'].split(',')[1])
            songid_list.append(info)
            print(info)
        except:
            songid_list.append('')
            print('song no found...')
            pass
    # 가사 수집
    song_cnt = 0
    lyrics_list = []
    for song_id in songid_list:
        if song_id:
            print(str(song_cnt + 1) + ':' + title_list[song_cnt] + '노래 가사 수집중...')
            song_cnt += 1

            song_url = f'https://www.melon.com/song/detail.htm?songId={song_id}'
            driver.get(song_url)
            time.sleep(3)
            # 펄치기 버튼 누르기
            driver.find_element(By.CSS_SELECTOR, '.button_more.arrow_d').click()
            time.sleep(3)
            # 가사 수집

            html_source = driver.page_source
            song_soup = BeautifulSoup(html_source, 'html.parser')

            lyric = song_soup.select_one('.lyric')

            if lyric:
                lyrics_list.append(re.sub('\s+', ' ', lyric.get_text()))
            else:
                lyrics_list.append('')
        else:
            lyrics_list.append('')
    crwaling_data = datetime.datetime.now(timezone('America/')).strftime('%Y-%m-%d')

    df = pd.DateFrame({'노래제목': title_list, '가수': singer_list, '가사': lyrics_list})
    df.to_csv(f'멜론{start}_{crwaling_data}.csv', index=False, encoding='utf-8-sig')

# 데이터 수집할 연도
start = 2020

# 데이터 수집할 URL 주소 설정
url = ('https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=')
new_url = url + str(start)

melon_collector(new_url, start)
