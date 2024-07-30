# import sys
# import csv
# import matplotlib.pyplot as plt
# from matplotlib import rc
#
# rc('font', family='AppleGothic')
# plt.rcParams['axes.unicode_minus'] = False
#
# csv.field_size_limit(sys.maxsize)
# # 1) 파일 읽기
# f = open('201902_201902_연령별인구현황_월간.csv', 'r', encoding='euc-kr')
# reader = csv.reader(f)
# res = []
# user = input("입력하세요")
# for row in reader:
#     # print(row)
#     # 신도림 지역에 정보만 가져와야 함
#     if user in row[0]:
#         print(row)
#         # 0 세부터 99세까지
#         for i in row[3]:
#             res.append(int(i.replace(',', '')))
#
# plt.title('{user}'.format(user=user))
# plt.plot(res)
# plt.show()

# # 교수님 코드
# import sys
# import csv
# import matplotlib.pyplot as plt
# from matplotlib import rc
#
# rc('font', family='AppleGothic')
# plt.rcParams['axes.unicode_minus'] = False
#
# csv.field_size_limit(sys.maxsize)
#
# # 1) 파일 읽기
# f = open('201902_201902_연령별인구현황_월간.csv', 'r', encoding='euc-kr')
# reader = csv.reader(f, delimiter=',')
# res = []
# si = input("시(광역시) 입력하세요")
# dong = input("동네명 입력하세요")
#
# for row in reader:
#     # print(row)
#     # 신도림 지역에 정보만 가져와야 함
#     if si in row[0] and dong in row[0]:
#         # 0 세부터 99세까지
#         for i in row[3]:
#             res.append(int(i.replace(',', '')))
#
# plt.title('{user}{dong}'.format(user=si, dong=dong))
# plt.plot(res)
# plt.style.use('ggplot')
# plt.show()
