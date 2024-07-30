# 임포트
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px
# import koreanize_matplotlib

import warnings

from matplotlib import rc

warnings.filterwarnings('ignore')
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# .sav은 통계 분석 소프트웨어 spss 전용 파일
# 2020년에 발간된 복지패널 데이터 (2019 조사 결과)

raw_welfare = pd.read_spss('../data_files/Koweps_hpwc14_2019_beta2.sav')
print(raw_welfare)

welfare = raw_welfare.copy()
welfare
#  변경할 컬럼의 이름을 dictionary  자료구조로 정의
col_names = {'h14_g3':'sex',
             'h14_g4':'birth',
             'h14_g10': 'marriage_type',
             'h14_g11': 'religion',
             'p1402_8aq1':'income',
             'h14_eco9':'code_job',
             'h14_reg7':'region'}
# 컬럼명 변경
welfare = welfare.rename(columns=col_names)
print('성별 데이터 탑입 확인:', welfare['sex'].dtype)
print('성별 데이터 결측치 확인:', welfare['sex'].isna().sum())
print('성별 빈도 확인')
welfare['sex'].value_counts()

# 코드로 되어 있는 성별(1.0,2.0) - > 문자열(male,female)변환
# 1.0 -> male, 2.0-> female

welfare['sex'] = np.where(welfare['sex']== 1.0, 'male','female')
print('성별의 변도 확인')
welfare['sex'].value_counts()

# 그래프로 확인
sns.countplot(welfare, x='sex')
plt.show()