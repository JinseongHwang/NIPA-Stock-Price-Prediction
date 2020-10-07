# 캔들 차트로 시각화 하기
# 캔들 차트로 하루의 거래 추세나 주가의 움직임 파악에 도움이 된다.

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

pd.set_option('display.max_columns', None)

# 주식 데이터 불러오기
data_frame = pd.read_csv('./stock.csv', index_col = ['Date'], parse_dates = True)

# 데이터 확인
print(data_frame)

# mplfinance 라이브러리를 사용하면 캔들 차트를 간편하게 시각화할 수 있다.
mc = mpf.make_marketcolors(up = 'r',down = 'b')
s = mpf.make_mpf_style(marketcolors = mc)
mpf.plot(data_frame, type = 'candle', figscale = 1.2, style = s, savefig = 'plot4.png')