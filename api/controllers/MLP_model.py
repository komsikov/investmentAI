from api import api
from api.ml.MLP_model import MLP_model

@api.route('/mlp/get_price', methods=['GET', 'POST'])
def get_mlp_price():
    price = MLP_model.run()
    return str(price)
