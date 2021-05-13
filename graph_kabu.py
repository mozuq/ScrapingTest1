import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import japanize_matplotlib


start = datetime.date(2000,1,1)
end = datetime.date(2021,3,31)
ai = web.DataReader('7259.T',"yahoo",start,end)

fig = plt.figure(figsize=(12, 8),facecolor='skyblue', tight_layout=True)

x = ai.index
y = ai['Close']
plt.plot(x,y,label='アイシン株価')

plt.grid()
plt.legend()

plt.show()
