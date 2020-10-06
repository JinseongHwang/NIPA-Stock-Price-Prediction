import pandas as pd
import xlrd

# 코로나 엑셀 파일 경로
xlpath = './corona_data.xlsx'

# pandas를 활용해 엑셀 파일을 불러와서, xldata라는 변수에 저장한다.
xldata = pd.read_excel(xlpath)

# 엑셀 데이터셋에서 필드명이 '확진자'인 데이터만 추출해서 출력한다.
confirmed_cases = xldata['확진자']
print(confirmed_cases)

print('=================================================================')

# .loc를 활용해서 '2020-07-30'의 사망자 데이터만 추출해서 출력한다.
# .loc[행 지정, 열 지정] 과 같은 형태로 입력받는다.
death_200730 = xldata.loc[xldata['날짜'] == '2020-07-30', '사망자']
print(death_200730)

print('=================================================================')

# .loc를 활용해서 '확진자' 수가 10,000 보다 큰 모든 데이터를 추출해서 출력한다.
# , 뒤에 ':'를 입력해주면 특정한 조건 없이 모든 데이터를 반환하라는 의미이다.
confirmed_over10000 = xldata.loc[xldata['확진자'] >= 10000, :]
print(confirmed_over10000)