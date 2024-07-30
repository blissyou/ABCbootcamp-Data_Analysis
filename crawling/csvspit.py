import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('csvfiles/flight_data_None.csv', encoding='utf-8-sig')

# 날짜시간 열에서 시간 부분을 제외하고 필요한 부분만 추출
def clean_date_time(date_time_str):
    # 날짜와 시간 부분을 추출
    date_part = date_time_str.split()[0]
    time_part = date_time_str.split('-')[-1][:5]  # 마지막 부분에서 HH:MM 추출
    return f"{date_part}-{time_part}"

# '날짜시간' 열을 원하는 형식으로 변환
df['날짜시간'] = df['날짜시간'].apply(clean_date_time)

# '날짜시간' 열을 datetime 형식으로 변환
df['날짜시간'] = pd.to_datetime(df['날짜시간'], format='%Y-%m-%d-%H:%M')

# '날짜시간' 열 기준으로 내림차순 정렬
df = df.sort_values(by='날짜시간', ascending=False)

# '날짜시간' 열을 다시 문자열 형식으로 변환
df['날짜시간'] = df['날짜시간'].dt.strftime('%Y-%m-%d-%H:%M')

# 변경된 데이터프레임을 새로운 CSV 파일로 저장
df.to_csv('네이버항공사_2024-08-01~2025-06-30_days_10.csv', index=False, encoding='utf-8-sig')

print(df.head())  # 첫 몇 개의 행을 출력하여 확인
