import csv

# 0) 최고 기온이 가장 높았던 날짜와 온도를 저장할 변수 선언

mix_data = ''  # 최고기온이 가장 높았던 날짜
mix_temp = 999  # 최고 기온이 가장 높았던 온도 -> 초기화를 극적인 값으로 설정

# 1) 파일을 연다
f = open('../data_files/seoul.csv', 'r', encoding='euc-kr')
# 1-2) 파일을 읽는다
data = csv.reader(f, delimiter=',')
# 1-3) 해더 저장
header = next(data)
# 2) 날짜, 최고 기온

for row in data:
    if row[-1] == '':
        row[-1] = 999

    # 최고 기온 형변환
    row[-1] = float(row[-1])

    # 2-3) 저장된 최고 기온과 현재 최고기온을 비교해서 더 높은 온도의 최고 기온과 날짜를 저장
    if max_temp > row[3]:
        max_data = row[0]
        max_temp = row[3]
print('기상 관층 이래 서울의 최고 기온이 가장높았던 날은', max_data, '최고기온은', max_temp, '입니다')

# 4) 파일 닫기
f.close()
