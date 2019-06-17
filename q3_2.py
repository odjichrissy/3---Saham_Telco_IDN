import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


df1 = pd.read_csv('EXCL.JK.csv',na_values = '-', parse_dates=['Date'])
df1_april = df1[(df1['Date'] > '2019-03-29') & (df1['Date'] < '2019-05-01')]
df2 = pd.read_csv('FREN.JK.csv',na_values = '-', parse_dates=['Date'])
df2_april = df2[(df2['Date'] > '2019-03-29') & (df2['Date'] < '2019-05-01')]
df3 = pd.read_csv('ISAT.JK.csv',na_values = '-', parse_dates=['Date'])
df3_april = df3[(df3['Date'] > '2019-03-29') & (df3['Date'] < '2019-05-01')]
df4 = pd.read_csv('TLKM.JK.csv',na_values = '-', parse_dates=['Date'])
df4_april = df4[(df4['Date'] > '2019-03-29') & (df4['Date'] < '2019-05-01')]

plt.figure('Harga Historis Saham Telco', figsize=(15,6))
plt.plot(df1_april['Date'], df1_april['Close'], color = 'red')
plt.plot(df2_april['Date'], df2_april['Close'], color = 'green')
plt.plot(df3_april['Date'], df3_april['Close'], color = 'cyan')
plt.plot(df4_april['Date'], df4_april['Close'], color = 'blue')


plt.title('Harga Historis Saham Telco Indonesia (April 2019)')
plt.ylabel('Rupiah(Rp)')
plt.xlabel('Tanggal')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.grid(True)
plt.legend(['PT XL','PT Smartfren','PT Indosat','PT Telekomunikasi'], loc='lower left')
plt.tight_layout()

plt.show()