# Plotting
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Numpy
import numpy as np

# Pandas
import pandas as pd
from pandas.tseries import offsets

from datetime import datetime

# name of graph
name = "aex-all-time-graph.png"

# define style
plt.style.use("bmh")

# load data
data = pd.read_csv("aex.csv") 

# Transform dates
data['Date'] = pd.to_datetime(data['Date']) 

# Figure
fig, ax = plt.subplots(2,1,figsize=(16, 12))
ax[0].plot(data['Date'], data['Close'], lw=1)
#ax.xlabel("Time")
ax[0].set_ylabel("Points")
ax[1].set_ylabel("Y/Y return [%]")
fig.suptitle("AEX index (Ex. Div) 3/1/1983 - 24/8/2021", fontsize=16)
ax[0].margins(0,0.1)

# vertical coloring
ax[0].axvspan(data['Date'].loc[0], data['Date'].loc[100], alpha=0.5, color='red')
ax[0].axvspan(data['Date'].loc[100], data['Date'].loc[200], alpha=0.5, color='green')

# Calculate annual and total return
year_range = max(data['Date']).year-min(data['Date']).year+1 # Number of years
return_data = pd.DataFrame(index=np.arange(year_range), data={'Year': np.arange(min(data['Date']).year, max(data['Date']).year + 1, 1)}) # Dataframe with the years as rows
return_data['Start'] = ''
return_data['Finish'] = ''
for i in np.arange(year_range):
    tmp = data.loc[data['Date'].dt.year == return_data['Year'].iloc[i]]
    return_data['Start'].iloc[i] = min(tmp['Date'])
    return_data['Finish'].iloc[i] = max(tmp['Date'])


return_data['Open'] = ''
return_data['Close'] = ''
for i in np.arange(year_range):
    tmp2 = data.loc[data['Date'] == return_data['Start'].iloc[i]]
    return_data['Open'].iloc[i] = tmp2['Close'].values[0]

    tmp3 = data.loc[data['Date'] == return_data['Finish'].iloc[i]]
    return_data['Close'].iloc[i] = tmp3['Close'].values[0]

return_data['Return'] = ((return_data['Close'] - return_data['Open']) / return_data['Open']) * 100
return_data['Return'] = np.around(return_data['Return'].astype(np.double), decimals=2)
total_annual_return = np.around((np.power(((return_data['Open'].iloc[38] - return_data['Open'].iloc[0]) / return_data['Open'].iloc[0])+1.0, 1.0/39.0)-1.0)*100, decimals=2)
print(total_annual_return)
print(return_data)

return_data.plot.bar(x='Year', y='Return', color='r', ax=ax[1], legend=False)
ax[1].axhline(y=total_annual_return, color='black', linestyle='-', linewidth=0.8)
ax[1].annotate("All time annual rate of return: 6.98%", xy=(1.2, 9))

# Calculate dividend reinvested

# X axis formatting
#year = mdates.MonthLocator(interval=12*4)
#ax.xaxis.set_major_locator(year)
#month = mdates.MonthLocator(interval=12)
#ax.xaxis.set_minor_locator(month)
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
#fig.autofmt_xdate()

# Annotations
#ax.plot(pd.to_datetime(['1983-01-03']), 45.38, 'bx')
#ax.annotate("Start data collection", xy=(pd.to_datetime(['1983-01-03']), 45.38),  xycoords='data',
#            xytext=(30, 50), textcoords='offset points',
#            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2"), ha='center')

# Annotations
#ax.plot(pd.to_datetime(['2021-08-24']), 783.15, 'bx')
#ax.annotate("Latest recorded data", xy=(pd.to_datetime(['2021-08-24']), 783.15),  xycoords='data',
#            xytext=(-100, 0), textcoords='offset points',
#            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2"), ha='center')

#ax.annotate('Labor Day', xy=('2012-9-4', 4850), xycoords='data', ha='center',
#            xytext=(0, -20), textcoords='offset points')
#ax.annotate('', xy=(pd.to_datetime(['1983-01-03']), 45.38),
#            xycoords='data', textcoords='data',
#            arrowprops={'arrowstyle': '|-|, widthA=6.2,widthB=0.2', })



# Save graph
plt.savefig(name, dpi=300)
plt.show()