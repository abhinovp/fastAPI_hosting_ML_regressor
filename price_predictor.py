import pickle
import numpy, pandas



class PredictPrice:

    def __init__(self) -> None:
        pass

    def load_xgb_model():

        with open(r'C:\Users\Echo\Desktop\python_projects\ml_app\core\models\toyota_rf_model','rb') as ph:
            PredictPrice.xgb_model = pickle.load(ph)
        
        print(" \n Model loaded")

        
    def get_sp(sample_input):
        
        sale_price = PredictPrice.xgb_model.predict(sample_input)

        return sale_price



