import yfinance as yf
import mplfinance as mpl
import pandas as pd
import datetime

excel_data = pd.read_excel("minervini.xlsx")
data = pd.DataFrame(excel_data, columns=["Stock", "RS_Rating", "50 Day MA", "150 Day Ma", "200 Day MA",
                                         "52 Week Low", "52 week High"])
stocks = [x[0] for x in data.values]

for stock in stocks:
    start = datetime.datetime.now() - datetime.timedelta(days=1000)
    end = datetime.date.today()
    stock_data = yf.download(stock, start, end)

    try:
        stock_cap = int(data.get_quote_yahoo(stock)["marketCap"])
        print(f"{stock_cap/1000000000} billion")
    except:
        print("index")

    mpl.plot(
        stock_data,
        figsize=(15, 7),
        mav=(50, 200),
        type='candle',
        title=stock,
        style="yahoo",
        show_nontrading=True,
        volume=True,
        warn_too_much_data=10000
    )

