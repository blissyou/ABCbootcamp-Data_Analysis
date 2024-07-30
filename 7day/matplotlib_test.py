import csv
import matplotlib.pyplot as plt

user = input("원하는 달을 입력하세요:")

f = open('../data_files/seoul.csv', 'r', encoding='euc-kr')
data = csv.reader(f, delimiter=',')
header = next(data)
high = []
low = []
avg = []
result = []

for row in data:
    if row[-1] != '' and row[-2] != '' and row[-3] != '':
        high.append(float(row[-1]))
        low.append(float(row[-2]))
        avg.append(float(row[-3]))

plt.title(f'seoul {user} ')
plt.hist(high, bins=100, color='r', label='%s month hight' % user)
plt.hist(avg, bins=100, color='g', label='%s month avg' % user)
plt.hist(low, bins=100, color='b', label='%s month low' % user)

plt.legend()
plt.show()
