from datetime import datetime
import xlrd
import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv('./stock.csv')

# 데이터 프레임 출력 : 데이터 프레임은 (행X열)형태로 이루어진 특수한 데이터 타입이다.
print(data_frame)

print('\n=======주식 데이터 살펴보기=======')

print('\n주식 데이터의 형태를 출력')
print(data_frame.shape) # (행, 열)

print('\n주식 데이터의 정보를 출력')
print(data_frame.info)

print('\n주식 데이터의 데이터 타입을 출력')
print(data_frame.dtypes)

print('\n주식 데이터의 상단 5개 행을 출력')
print(data_frame.head())

print('\n주식 데이터의 하단 5개 행을 출력')
print(data_frame.tail())

print('\n주식 데이터의 모든 열을 출력')
print(data_frame.columns)

print('\n주식 데이터의 요약 통계 자료 출력')
print(data_frame.describe())