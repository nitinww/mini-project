import pandas as pd
import numpy as np

df1 = pd.read_html("https://www.moneycontrol.com/financials/coalindia/balance-sheetVI/CI11/")
df2 = pd.read_html("https://www.moneycontrol.com/financials/coalindia/balance-sheetVI/CI11/2")
df3 = pd.read_html("https://www.moneycontrol.com/financials/coalindia/balance-sheetVI/CI11/3")
df4 = pd.read_html("https://www.moneycontrol.com/financials/coalindia/balance-sheetVI/CI11/4")

df1 = df1[0]
df1.set_index(0, inplace=True)
df1 = df1.iloc[:, ::-1]
df1 = df1.dropna(axis=1, how='all')
# new_header = df1.iloc[0]
# df1 = df1[1:]
# df1.columns = new_header
# df1 = df1[1:]
print(df1)
df2 = df2[0]
df2.set_index(0, inplace=True)
df2 = df2.iloc[:, ::-1]
df2 = df2.dropna(axis=1, how='all')
df3 = df3[0]
df3.set_index(0, inplace=True)
df3 = df3.iloc[:, ::-1]
df3 = df3.dropna(axis=1, how='all')
df4 = df4[0]
df4.set_index(0, inplace=True)
df4 = df4.iloc[:, ::-1]
df4 = df4.dropna(axis=1, how='all')

df1 = pd.DataFrame(df1)
df2 = pd.DataFrame(df2)
df3 = pd.DataFrame(df3)
df4 = pd.DataFrame(df4)

df = pd.concat([df4, df3, df2, df1], axis=1) 
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header

df.to_csv('COALINDIA-BS.csv')

df = pd.read_csv("COALINDIA-BS.csv")
print(df)
