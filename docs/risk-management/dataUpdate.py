# save_spy_data.py
# Download SPY data (proxy for S&P 500)


import pandas_datareader as web

# Fetch data from Stooq
data = web.DataReader('^SPX', 'stooq', start='2010-01-01', end='2024-12-31')
data = data.sort_index()  # chronological order

# Save to Excel
data.to_excel("data/SPX_data_stooq.xlsx")
print("Saved to SPX_data_stooq.xlsx")