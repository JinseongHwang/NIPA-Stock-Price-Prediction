# 주가, 이동평균선 시각화 하기

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

"""
종가: 해당 날짜의 마감 주가
이동평균: 해당 날짜의 이전 N일 간의 평균치
이격도: 주가와 이동평균 간의 차이 비율
"""

pd.set_option('display.max_columns', None)

# 주식 데이터 불러오기
data_frame = pd.read_csv('./stock.csv') 

# 수정 종가 이동평균(MA: Moving Average) 값 구하기
# .rolling(window = n): 데이터를 n개 행씩 묶어서 계산
# .mean(): 값들의 평균을 계산
ma5 = data_frame['Adj Close'].rolling(window = 5).mean() # 수정 종가 5일 이동평균
ma20 = data_frame['Adj Close'].rolling(window = 20).mean() # 수정 종가 20일 이동평균
ma60 = data_frame['Adj Close'].rolling(window = 60).mean() # 수정 종가 60일 이동평균

# 이동평균 값 추가하기
# .insert(): 데이터 프레임에 새로운 열 삽입
data_frame.insert(len(data_frame.columns), "MA5", ma5) # 'MA5'라는 열 이름으로 ma5 값 추가
data_frame.insert(len(data_frame.columns), "MA20", ma20) # 'MA20'라는 열 이름으로 ma20 값 추가
data_frame.insert(len(data_frame.columns), "MA60", ma60) # 'MA60'라는 열 이름으로 ma60 값 추가

# 거래량 5일 이동평균 추가
vma5 = data_frame['Volume'].rolling(window = 5).mean() # 거래량의 5일 이동평균 구하기
data_frame.insert(len(data_frame.columns), "VMA5", vma5) # 'VMA5'라는 열 이름으로 vma5 값 추가

# ======= 이격도 추가 =======
# 수정 종가 데이터를 5일 이동평균 값으로 나눈 비율
disp5 = (data_frame['Adj Close']/data_frame['MA5']) * 100

# 이격도 데이터를 'Disp5'라는 열 이름으로 추가
data_frame.insert(len(data_frame.columns), "Disp5", disp5) 

# 당일 종가가 아니라 다음 날 종가를 새로운 컬럼으로 추가하기
# shift(-1) 옵션을 사용하여 데이터를 하루씩 밀어서 삽입
# .shift(n): 데이터를 행 단위로 n칸씩 밀어낸다.
data_frame['tomorrow Adj Close']= data_frame['Adj Close'].shift(-1)

# 주가 변동 및 변동률(%) 추가하기 - 기대 수익률 계산 가능
data_frame['Fluctuation'] = data_frame['tomorrow Adj Close'] - data_frame['Adj Close'] # 주가 변동 데이터(다음날 종가 - 오늘 종가)
data_frame['Fluctuation Rate'] = data_frame['Fluctuation'] / data_frame['Adj Close'] # 주가 변동률 데이터(변동 / 오늘 종가)

# 데이터 확인
print(data_frame)

# 이동평균선의 시각화
# plt.plot(data_frame.index, data_frame['Adj Close'], label = 'Adj Close') # 수정 종가 시각화
# plt.plot(data_frame.index, data_frame['MA5'], label = 'MA5') # 이동평균선 시각화
plt.plot(data_frame['Adj Close'], label="Adj Close") # 수정 종가
plt.plot(data_frame['MA5'], label="MA5") # 종가 5일 이동평균
plt.plot(data_frame['MA20'], label="MA20") # 종가 20일 이동평균
plt.plot(data_frame['MA60'], label="MA60") # 종가 60일 이동평균

# 시각화 옵션 코드
plt.legend(loc = 'best')
plt.xticks(rotation = 45)
plt.grid()
plt.savefig('plot1.png')
plt.show()