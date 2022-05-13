import tensorflow as tf
# import numpy as np
# import pandas_datareader.data as pdr
import yfinance as fix

from api.ml.Data_gen import Data_gen, data_path
from api.ml.preprocessing import Data_processing

fix.pdr_override()

start = "2003-01-01"
end = "2018-01-01"

class MLP_model:

    def run():
        data_gen = Data_gen()
        data_gen.get_stock_data("AAPL", start_date=start, end_date=end)
        process = Data_processing(data_path + "/stock_prices.csv", 0.9)
        process.gen_test(10)
        process.gen_train(10)

        X_train = process.X_train / 200
        Y_train = process.Y_train / 200

        X_test = process.X_test / 200
        Y_test = process.Y_test / 200

        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(1, activation=tf.nn.relu))

        model.compile(optimizer="adam", loss="mean_squared_error")

        model.fit(X_train, Y_train, epochs=100)

        predicted_price = model.evaluate(X_test, Y_test)

        return predicted_price

        # If instead of a full backtest, you just want to see how accurate the model is for a particular prediction, run this:
        # data = pdr.get_data_yahoo("AAPL", "2017-12-19", "2018-01-03")
        # stock = data["Adj Close"]
        # X_predict = np.array(stock).reshape((1, 10)) / 200
        # print(model.predict(X_predict)*200)
