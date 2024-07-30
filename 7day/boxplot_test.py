import csv
import matplotlib.pyplot as plt

f = open('../data_files/seoul.csv', 'r', encoding='euc-kr')
data = csv.reader(f, delimiter=',')

# 결측치를 제외한 데이터만 시각화
# 1) 1월달 최고기온 , 8월달 최고기온 담을 리스트 변수 선언
jan_temp = []
aug_temp = []

# 2) 01월, 08월의 최고기온 데이터 추출

header = next(data)

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '01':
            jan_temp.append(float(row[-1]))
        if row[0].split('-')[1] == '08':
            aug_temp.append(float(row[-1]))

    # 2-3) 저장된 최고 기온과 현재 최고기온을 비교해서 더 높은 온도의 최고 기온과 날짜를 저장
plt.boxplot([jan_temp,aug_temp])
plt.xticks([1,2],['Jan','Aug'])

plt.show()
