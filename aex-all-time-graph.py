import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

from pandas.tseries import offsets

# name of graph
name = "aex-all-time-graph.png"

# define style
plt.style.use("bmh")

# load data
data = pd.read_csv("aex.csv") 

# Transform dates
data['Date'] = pd.to_datetime(data['Date']) 

print(datetime.today() - offsets.YearBegin())


# Figure
plt.figure(figsize=(18,7))
plt.plot(data['Date'], data['Close'], lw=1)
plt.xlabel("Time")
plt.ylabel("Points")
plt.title("AEX index (Ex. Div) 3/1/1983 - 24/8/2021")

# Save graph
plt.savefig(name, dpi=300)

plt.show()