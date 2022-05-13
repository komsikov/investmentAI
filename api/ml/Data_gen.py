from os.path import dirname, realpath
import pandas_datareader.data as pdr
import yfinance as fix
import time

fix.pdr_override()

data_path =  f"{dirname(realpath(__file__))}/data"

class Data_gen:
    """:data huyata"""

    def __init__(self) -> None:
        self.get_stock_data("AAPL", "2018-05-01", "2022-06-01")
        self.get_sp500("2018-05-01", "2018-06-01")

    def get_stock_data(self, ticker, start_date, end_date):
        """
        Gets historical stock data of given tickers between dates
        :param ticker: company, or companies whose data is to fetched
        :type ticker: string or list of strings
        :param start_date: starting date for stock prices
        :type start_date: string of date "YYYY-mm-dd"
        :param end_date: end date for stock prices
        :type end_date: string of date "YYYY-mm-dd"
        :return: stock_data.csv
        """

        i = 1

        try:
            all_data = pdr.get_data_yahoo(ticker, start_date, end_date)
        except ValueError:
            print("ValueError, trying again")

            i += 1

            if i < 5:
                time.sleep(10)
                self.get_stock_data(ticker, start_date, end_date)
            else:
                print("Tried 5 times, Yahoo error. Trying after 2 minutes")
                time.sleep(120)
                self.get_stock_data(ticker, start_date, end_date)

        stock_data = all_data["Adj Close"]
        stock_data.to_csv(f"{data_path}/stock_prices.csv")


    def get_sp500(self, start_date, end_date):
        """
        Gets sp500 price data
        :param start_date: starting date for sp500 prices
        :type start_date: string of date "Y-m-d"
        :param end_date: end date for sp500 prices
        :type end_date: string of date "Y-m-d"
        :return: sp500_data.csv
        """

        i = 1

        try:
            sp500_all_data = pdr.get_data_yahoo("SPY", start_date, end_date)
        except ValueError:
            print("ValueError, trying again")

            i += 1

            if i < 5:
                time.sleep(10)
                self.get_stock_data(start_date, end_date)
            else:
                print("Tried 5 times, Yahoo error. Trying after 2 minutes")
                time.sleep(120)
                self.get_stock_data(start_date, end_date)

        sp500_data = sp500_all_data["Adj Close"]

        sp500_data.to_csv(f"{data_path}/sp500_data.csv")
