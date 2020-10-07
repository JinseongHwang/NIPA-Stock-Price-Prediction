# 변동률 분포 시각화 하기
# 히스토그램 또는 커널 밀도 추정 그래프(KDE) 로 확인 가능하다.

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

# 히스토그램을 이용해 분포 살피기
# 히스토그램으로 데이터의 분포를 살펴보면, 어떤 값에 치중되어 있는지, 이상치(outlier)가 있는지 등을 직관적으로 파악 가능하다.
data_frame['Fluctuation Rate'].plot.hist()
plt.title('Fluctuation Rate Histogram')

# 현재까지 그려진 그래프를 보여줌
plt.savefig('plot3-1.png')
plt.show()

# 그래프 초기화
plt.cla()

# 커널 밀도함수를 이용해 분포 살피기
# 수학적 정의를 내리는 것은 어려우므로, 그저 히스토그램을 조금 더 부드럽게 표현하는 형태라고 알고 넘어가자.
data_frame['Fluctuation Rate'].plot.kde()
plt.title('Fluctuation Rate KDE plot')

# 현재까지 그려진 그래프를 보여줌
plt.savefig('plot3-2.png')
plt.show()