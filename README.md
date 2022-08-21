# Growth-Stock-finder
You can find and analyse potential growth stocks.

## How to set it up:
  In order for the scripts to work you have to install the following packages:
  pandas, yfinance, yahoo_fin, mplfinance

  You can do it by typeing the following commands into your command prompt line by line (these include dependencies):
  - pip install numpy
  - pip install python-dateutil
  - pip install pytz
  - pip install matplotlib
  - pip install pandas
  - pip install yfinance
  - pip install yahoo_fin
  - pip install mplfinance

## How to use:
  1. Run the script called "find_growth_stocks.py" it may not succed at first try, try again and make sure you
  you have a stable internet connection.
  2. You will see that a bunch of csv files (named as the top 30% performing stocks of the S&P500) and a exel file named "minervini.xlsx" have been created
  3. In the excel file you can find the stocks which made the Minervini requirements ordered by their RS rating
  4. If you want you can have a look at the value, 200 and 50 day moving averages, and volume of the sotcks in the "minervini.xlsx" in the last 1000 days do this:
     - Run the scipt named "plot.py"
     - You can see the value of the stock as the candlestick chart, the 50 day moving average as the blue and the 200 day moving average as the orange line, on the bottom you can see the volume of the stock
     - You can use the zoom tool to zoom in
     - If you want to move from one chart to an other simply close the current one
