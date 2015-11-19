from pylab import *
import matplotlib.pyplot as plt
from datetime import datetime
import time
from matplotlib.dates import DateFormatter, WeekdayLocator, HourLocator, DayLocator, MONDAY
from matplotlib.finance import candlestick, plot_day_summary, candlestick2

mondays = WeekdayLocator(MONDAY)
alldays = DayLocator()
weekFormatter = DateFormatter('%b %d')
dayFormatter = DateFormatter('%d')

Date1 = '01/01/2010'
Date2 = '02/01/2010'

Date1 = date2num(datetime.strptime(Date1, "%d/%m/%Y"))
Date2 = date2num(datetime.strptime(Date2, "%d/%m/%Y"))
#so redefining the Prices list of tuples...
Prices = [(Date1, 1.123, 1.212, 1.463, 1.056), (Date2,1.121, 1.216, 1.498, 1.002)]
#and then following the official example. 
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
candlestick(ax, Prices, width=0.6)

ax.xaxis_date()
ax.autoscale_view()
plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()
