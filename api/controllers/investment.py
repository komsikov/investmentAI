from api import api
from api.ml.Data_gen import Data_gen, data_path
from api.ml.preprocessing import Data_processing
from api.ml.back_test import back_test

@api.route('/data_gen')
def start():
    Data_gen()
    return "Done"

@api.route('/back_test', methods=['GET', 'POST'])
def backtest(strategy, seq_len, ticker, start_date, end_date, dim):
    result = back_test(strategy, seq_len, ticker, start_date, end_date, dim)
    return result
    
@api.route('/preprocessing', methods=['GET', 'POST'])
def preprocessing():
    processing = Data_processing(f"{data_path}/stock_prices.csv", 0.9)

    processing.gen_train()

    return "Done"