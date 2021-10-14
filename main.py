#imports
from typing import Dict, List
from fastapi import FastAPI, Request
from pydantic import BaseModel
import json

#defining class objects for ML predictors and classifiers

# object model that helps absorb predictors input parameters
class Predict_struct(BaseModel):
    model_number : int
    year : int
    mileage : int
    tax : int
    mpg : int
    enginesize : int
    automatic : int
    manual : int
    semiauto : int
    diesel : int
    hybrid : int
    other : int
    petrol : int

# object model that helps common input
class Common_struct(BaseModel):
    predict : str
    classify : str
    predict_input_set : Predict_struct


# object model that helps absorb classfiers input parameters
class Classify_struct(BaseModel):
    name : str

#data access classes
# SETUP CLASSES CALL

from core.models.price_predictor import PredictPrice as ppr
# Load model once
ppr.load_xgb_model()

# sample input
# format: 	model	year   mileage	tax	mpg	engineSize	Automatic	Manual	Semi-Auto	Diesel	Hybrid	Other	Petrol
sample_input = [[5,2019,516,150,33.2,2.0,0,1,0,0,0,0,1]]

mlapp = FastAPI()

# Rolling callers
# base call
@mlapp.get("/v1/")
def base():
    return {"message":" This is the base for ML apps"}

@mlapp.post("/v1/")
async def postbase(request: Request):
    return {"message":" This is the base for ML apps"}

# post call
@mlapp.post("/v1/algos")
async def ml_decision(incoming_json : Common_struct):
    mn = json.loads(incoming_json.json())
    #print(mn['predict_input_set']['year'])
    print(type(mn['predict_input_set']['year']))

    to_predict_list = [ mn['predict_input_set']['model_number'],
    mn['predict_input_set']['year'],
    mn['predict_input_set']['mileage'],
    mn['predict_input_set']['tax'],
    mn['predict_input_set']['mpg'],
    mn['predict_input_set']['enginesize'],
    mn['predict_input_set']['automatic'],
    mn['predict_input_set']['manual'],
    mn['predict_input_set']['semiauto'],
    mn['predict_input_set']['diesel'],
    mn['predict_input_set']['hybrid'],
    mn['predict_input_set']['other'],
    mn['predict_input_set']['petrol']
    ]

    result_price = ppr.get_sp([to_predict_list])

    print("Sale price is : ",result_price) #)incoming_json.json())
    return_dict = { "message" : " Below is the approx current value for your toyota",
            "Sale_Price": str(result_price) }

    return  json.dumps(return_dict) #incoming_json.json()


