import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
# df_mpg = pd.read_csv('data_files/mpg.csv')
# df_new = df_mpg.copy()  #복사본 만들기
# df_new.rename(columns={'manufacturer': 'manufact'})
#
# print(df_new)

# 통합연비 구하기 => (도시연비 + 고속도로 연비)/2

df_mpg = pd.read_csv('../data_files/mpg.csv')
df_new = df_mpg.copy()  #복사본 만들기
df_mpg['total'] = ((df_mpg['cty'] + df_mpg['hwy']) / 2)
# 합격 불합격 조건 통합연비 구하기
# 통합 토탈 기준 20이상이면 pass 이하면 fail
df_mpg['test'] = np.where(df_mpg['total'] >= 20, 'pass', 'fail')
# total 연비 를 그래프로 시각화
plt.hist(df_mpg['total'])

# test 컬럼 막대그래프로 시각화 polt.bar(rot = 0) rot는 글자 로테이션
# df_mpg['test'].value_counts().plot.bar(rot=0)

# plt.title("합격율")
# df_mpg['test'].value_counts().plot.pie(autopct='%1.1f%%')
#
# plt.show()
print(df_mpg['category'].unique())

# df_mpg category 2seater인 경우만 추출

print(df_mpg.query("category=='minivan'"))

# df_mpg year가 2000을 초과하는 경우

print(df_mpg.query("year>2000"))

# 여러가지 조건으로 충족하는 행 추출하기
# minvan이면서 연식이 2000년이상인 경우만 데이터 추출
print(df_mpg.query("category == 'minivan' & year>=2000"))

# 차중이 minivan ,2seater, pickup인경우만 데이터 추출
print(df_mpg.query("category == 'minivan' | category == '2seater'|category == 'pickup'"))
print(df_mpg.query("category in ['minivan', '2seater' , 'pickup']"))

# 여러개 컬럼 한번에 제거
df_mpg.drop(columns='year')

# 연식 기준으로 데이터 정렬 -> 기본 오름차순 (작은것에서 큰것을 정렬)

print(df_mpg.sort_values('year', ascending=True))
# 파생변수 추가

print(df_mpg.assign(total=((df_mpg['cty'] + df_mpg['hwy']) / 2)))
