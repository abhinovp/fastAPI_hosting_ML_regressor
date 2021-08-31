from enum import Enum
from typing import Optional
import os
from fastapi import FastAPI, Request, Form, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.dac_filters import StoreClassifiers as scs
from fastapi.responses import HTMLResponse


app = FastAPI()
templates = Jinja2Templates(directory=os.path.abspath(os.path.expanduser('templates')))
scsobj = scs()
app.mount("/static", StaticFiles(directory="static"), name="static")

#Calling DAClass for Mysql>Df conversion: Returns 2 DFs
orders,customers = scs.generate_df_from_mysql()

class serviceChoices(str, Enum):
    svc = "svc"
    trc = "trc"
    lbc = "lbc"
    totr =  "totr"

@app.get("/")
def root_go():
    return {"message": "Go step 2"}


@app.get("/form",response_class=HTMLResponse)
def form_post(request: Request):
    result = "Type a service name"
    return templates.TemplateResponse('result.html', context={'request': request, 'result': result})



@app.post("/form",response_class=HTMLResponse)
def form_post(request: Request,
              classi_dd: serviceChoices = Form(serviceChoices.svc),
              ):

    if classi_dd.strip() ==  "lbc":
        result = scsobj.get_loyal_member(customers)
    elif classi_dd == "svc":
        result = scsobj.get_senior_customer(customers)
    elif classi_dd == "trc":
        result = scsobj.get_top_revenue_customer(orders,customers)
    elif classi_dd == "totr":
        result = scsobj.get_total_revenue(orders)
    else:
        result = "Wrong Input"

    html_content = """
        <html>
            <head>
                <title>Result is : </title>
            </head>
            <body>
                <h3>"""+result+"""</h3>
            </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)

