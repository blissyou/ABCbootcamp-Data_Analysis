import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
file_path = 'flight_도쿄.csv'
data = pd.read_csv(file_path,encoding=)

# 데이터 타입 변환 및 정리
data['날짜시간'] = pd.to_datetime(data['날짜시간'], errors='coerce')
data['가격'] = data['가격'].str.replace(',', '').astype(float)

# 데이터 시각화
plt.figure(figsize=(14, 7))
plt.plot(data['날짜시간'], data['가격'], marker='o', linestyle='-', color='b')
plt.title('비행기 가격 변화')
plt.xlabel('날짜시간')
plt.ylabel('가격')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 시각화 결과 저장
plt.savefig('/mnt/data/flight_price_trend.png')
plt.show()
