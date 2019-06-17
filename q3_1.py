import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df1 = pd.read_csv('EXCL.JK.csv',na_values = '-')
df2 = pd.read_csv('FREN.JK.csv',na_values = '-')
df3 = pd.read_csv('ISAT.JK.csv',na_values = '-')
df4 = pd.read_csv('TLKM.JK.csv',na_values = '-')

plt.figure('Harga Historis Saham Telco', figsize=(15,6))

plt.plot(df1['Date'], df1['Close'], 'r-')
plt.plot(df2['Date'], df2['Close'], 'g-')
plt.plot(df3['Date'], df3['Close'], 'b-')
plt.plot(df4['Date'], df4['Close'], 'c-')


plt.title('Harga Historis Saham Telco Indonesia')
plt.ylabel('Rupiah(Rp)')
plt.xlabel('Tanggal')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.grid(True)
plt.legend(['PT XL','PT Smartfren','PT Indosat','PT Telekomunikasi'], loc='lower left')
plt.tight_layout()


plt.show()