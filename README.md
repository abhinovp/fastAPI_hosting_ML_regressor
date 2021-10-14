<h1> Hosting a Machine Learning model over a FASTAPI server. </h1>

Purpose: To predict sale price of a used toyota car and to send details of the car through a JSON request.

## Step 1: Load the files in the below format

ML_Price_Prediction
|
|--models
|    |-- picklefile
|    |-- ML_full_trained_model.ipynb
|    |-- price_predictor.py
|--v1
|main.py

![alt text](https://github.com/ippudkippude/fastAPI/blob/main/fold_struct.PNG)

## Step 2: Start uvicorn instance on cmd/powershell

![alt text](https://github.com/ippudkippude/fastAPI/blob/main/uvi_postman.PNG)

## Step 3: From Postman use a request format JSON as below to include car details and POST:

{
    "predict": "True",
    "classify": "False",
    "predict_input_set": {
        "model_number": 10,
        "year": 2012,
        "mileage": 15106,
        "tax": 257,
        "mpg": 22,
        "enginesize": 1.0,
        "automatic": 1,
        "manual": 1,
        "semiauto": 0,
        "diesel": 0,
        "hybrid": 0,
        "other": 0,
        "petrol": 1}
    
}


## Sample output(JSON) :

"{\"message\": \" Below is the approx current value for your toyota\", \"Sale_Price\": \"[8129.29]\"}"
