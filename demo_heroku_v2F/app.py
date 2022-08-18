# import necessary libraries and dependencies
from pickle import load
import numpy as np
from flask import Flask, render_template, request

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
import json
import numpy as np
import pandas as pd

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Load ML Model
#################################################
model = load(open('./models/linear_regression_model.pt', 'rb'))
model2 = load(open('./models/finalizedsvm_model.pt', 'rb'))
model3 = load(open('./models/finalizedregr_model.pt', 'rb'))

# create route that renders home.html template
@app.route("/")
def home():

    return render_template("index.html")

# create route that renders datatable.html template
@app.route("/datatable")
def datatable():
       
    # converting csv to html
    data = pd.read_csv("./static/data/column_name_key_rev.md.csv")
    return render_template("datatable.html", tables=[data.to_html(index=False)], titles=[''])

    # return render_template("datatable.html")

# create route that renders model.html template
@app.route("/mlearning")
def mlearning():

        return render_template("mlearning.html")


# create route that renders prediction.html template
@app.route("/prediction")
def prediction():

    # # Method 1 inputs
    # cylinders = ""
    # displacement = ""
    # horsepower = ""
    # weight = ""
    # acceleration = ""

    prediction_text = ""

    return render_template("prediction.html", result = prediction_text)


# Query the database and send the jsonified results
@app.route("/send", methods=["POST"])
def send():

    # # Method 1:  Obtain form inputs and add to numpy array or dataframe
    models = request.form["model"]
    PM25 = float(request.form["PM25"])
    LandEQI = float(request.form["landeqi"])
    SociodEQI = float(request.form["sociodeq"])
    BuiltEQI = float(request.form['builteqi'])
    clu501 = float(request.form["CLU50"])
    PM10 = float(request.form["SO2"])
    SO2 = float(request.form["SO2"])
    NO2 = float(request.form["NO2"])
    O3 = float(request.form["O3"])
    CO = float(request.form["CO"])
    CN = float(request.form["CN"])
    diesel = float(request.form["diesel"])
    CS2 = float(request.form["CS2"])
    airEQI = float(request.form["airEQI"])
    waterEQI = float(request.form["waterEQI"])
    lci = float(request.form["LCI"])
    uci = float(request.form["UCI"])

    features = [PM25, LandEQI, SociodEQI, BuiltEQI, clu501, PM10, SO2, NO2, O3, CO, CN, diesel, CS2, airEQI, waterEQI, lci, uci]

    print(features)

    # Method 2:  Obtain form inputs and add to numpy array; note: order of variables must match X array in ML model 
    # features = [float(x) for x in request.form.values()]

    # convert list to numpy array (all values must be numerical for prediction to work)
    final_features = [np.array(features)]

    # use form results to make prediction
    if models == "1":
        prediction = model.predict(final_features)[0]
    elif models == "2":
        prediction = model2.predict(final_features)[0]
    else:
        prediction = model3.predict(final_features)[0]


    # create html content - either single variable, dictionary, or string
    prediction_text = f"Only considering air quality factors, there is expected to be {round(prediction,1)} cases of lung cancer fatality per 100,000 people."

    # send prediction to html page
    return render_template("prediction.html", result = prediction_text)


if __name__ == "__main__":
    app.run()
