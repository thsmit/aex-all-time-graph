#import bisect
#import datetime
#from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pandas as pd
from datetime import datetime

from pandas.plotting import table

#define the ticker symbol
#tickerSymbol = '^AEX'

#get data on this ticker
#tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
#tickerDf = tickerData.history(period='1d', start='1983-1-3', end='2021-8-24')

#see your data
#print(tickerDf)

#tickerDf['Close'].plot()

fname = "aex-all-time-graph.png"

#plt.style.use('ggplot')
#plt.style.use("dark_background")
plt.style.use("bmh")


tickerDf = pd.read_csv("aex.csv") 
tickerDf['Date'] = pd.to_datetime(tickerDf['Date'])



plt.figure(figsize=(18,7))
plt.plot(tickerDf['Date'], tickerDf['Close'], lw=1)
plt.xlabel("Time")
plt.ylabel("Points")
plt.title("AEX index (Ex. Div) 3/1/1983 - 24/8/2021")

# plt.rcParams.update(plt.rcParamsDefault)
# face = "w"
# edge = "k"

# h, w = 13, 9
# fig, ax = plt.subplots(figsize=(w, h))
# ax.set_axis_off()
    
    # fig.suptitle("Calendar of life", y=0.89)
    # birthday = datetime.date(1990, 3, 17)
    # today = datetime.date.today()
    # life = [
    #     ("born", birthday),
    #     ("early childhood", birthday + datetime.timedelta(days=4.15 * 365)),
    #     ("school", datetime.date(2003, 8, 18)),
    #     ("high school", datetime.date(2009, 9, 1)),
    #     ("university", datetime.date(2017, 7, 13)),
    #     ("work", datetime.date(2018, 10, 1)),
    #     ("freelance engineer", datetime.date(2019, 7, 1)),
    #     ("phd", today),
    # ]

    # stages = [key for key, date in life]
    # weeks_of_life = [round((date - birthday).days / 7) for key, date in life]
    # weeks_of_life_past = np.cumsum(np.diff(weeks_of_life))

    # data = defaultdict(list)
    # colors = {
    #     "early childhood": "C0",
    #     "school": "C1",
    #     "high school": "C2",
    #     "university": "C3",
    #     "freelance engineer": "C8",
    #     "phd": "C6",
    #     "work": "C4",
    #     "future": face,
    # }
    # week_num = 0
    # weeks = np.linspace(0, h, 52)
    # years = np.linspace(w, 0, 80)
    # for i, year in enumerate(years):
    #     for j, week in enumerate(weeks):
    #         week_num += 1
    #         index = bisect.bisect_left(weeks_of_life_past, week_num) + 1
    #         if index == len(weeks_of_life_past) + 1:
    #             stage = "future"
    #         else:
    #             stage = stages[index]
    #         data[stage].append((week, year))

    # for k, v in data.items():
    #     ax.scatter(*zip(*v), edgecolors=edge, facecolor=colors[k], label=k)

    # for i, year in enumerate(years):
    #     if i % 10 == 0 and i > 0:
    #         ax.text(
    #             -0.2,
    #             year,
    #             f"{i}y",
    #             horizontalalignment="right",
    #             verticalalignment="center",
    #             fontsize=9,
    #         )
plt.legend()
plt.savefig(fname, dpi=300)
plt.show()
