# 변동률 시각화 하기

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

# 주식 데이터 불러오기
data_frame = pd.read_csv('./stock.csv') 

# 당일 종가가 아니라 다음 날 종가를 새로운 컬럼으로 추가하기
# shift(-1) 옵션을 사용하여 데이터를 하루씩 밀어서 삽입
# .shift(n): 데이터를 행 단위로 n칸씩 밀어낸다.
data_frame['tomorrow Adj Close']= data_frame['Adj Close'].shift(-1)

# 주가 변동 및 변동률(%) 추가하기 - 기대 수익률 계산 가능
data_frame['Fluctuation'] = data_frame['tomorrow Adj Close'] - data_frame['Adj Close'] # 주가 변동 데이터(다음날 종가 - 오늘 종가)
data_frame['Fluctuation Rate'] = data_frame['Fluctuation'] / data_frame['Adj Close'] # 주가 변동률 데이터(변동 / 오늘 종가)

# 데이터 확인
print(data_frame)

# 변동률의 시각화
plt.figure(figsize = (12, 8)) # 표현할 그래프의 크기 설정
plt.plot(data_frame.index, data_frame['Fluctuation Rate']) # 변동률 데이터 시각화
plt.axhline(y = 0, color = 'red', ls = '--') # 변동률 폭을 관찰하기 위한 기준 수평선 추가

"""
이 코드의 결과에는 빨간 0점 선을 기준으로 위아래로 출렁이는 형태의 그래프를 확인할 수 있다.
이와 같이 시간 속성을 가지고 있는 데이터를 "시계열 데이터(Time Serise Data)"라고 부른다.
그래프를 보면, ±0.01 등락율 분포가 가장 많고, ±0.04 보다 큰 등락율을 가지는 경우는 거의 없는 것을 확인할 수 있다.
이는 삼성전자 주식 데이터이며, 대형주이기 때문에 변동이 적고, 단타족에게 선호되지 않는 형태이다.
"""

# 시각화 옵션 코드
plt.legend(loc = 'best')
plt.grid()
plt.savefig('plot2.png')
plt.show()