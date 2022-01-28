import yfinance as yf

# guide to yfinance
# https://pypi.org/project/yfinance/

# how to work with Pandas = Python Data Analysis Library
# https://datacarpentry.org/python-ecology-lesson/


stock = 'AMZN'

qbs = yf.Ticker(stock).quarterly_balance_sheet

print(type(qbs))
print()
print(qbs)
print()
print('columns :  ', qbs.columns)
print()
print('shape :  ', qbs.shape)
print('head : ')
print(qbs.head(2))
print('tail : ')
print(qbs.tail(2))
print()
print( qbs.iloc[22, 0] )
print( qbs.iloc[21, 0] )   # iloc is position based
print()


AP = qbs.loc[['Accounts Payable'], :]     # loc is label based
AP = AP.iloc[0, 0]
print('AP = ', AP)


LTD = qbs.loc[['Long Term Debt'], :]
LTD = LTD.iloc[0, 0]
print('LTD = ', LTD)


news = yf.Ticker(stock).news
print(news)



