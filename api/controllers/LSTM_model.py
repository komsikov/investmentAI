from api import api
from api.ml.LSTM_model import LSTM_model

@api.route('/lstm/get_price', methods=['GET', 'POST'])
def get_lstm_price():
    price = LSTM_model.run()
    return str(price)