# import necessary libraries
from pickle import load
import numpy as np
from flask import Flask, render_template, request

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Load ML Model
#################################################
model = load(open('./models/model_linregress_2022081800.pkl', 'rb'))

# create route that renders index.html template
@app.route("/")
def home():

    # # Method 1 inputs
    # cylinders = ""
    # displacement = ""
    # horsepower = ""
    # weight = ""
    # acceleration = ""

    prediction_text = ""

    return render_template("index.html", result = prediction_text)


# Query the database and send the jsonified results
@app.route("/send", methods=["POST"])
def send():

    # # Method 1:  Obtain form inputs and add to numpy array or dataframe
    # cylinders = float(request.form["mpgCylinders"])
    # displacement = float(request.form["mgpDisplacement"])
    # horsepower = float(request.form["mpgHP"])
    # weight = float(request.form["mpgWeight"])
    # acceleration = float(request.form['mpgAcceleration'])

    # features = [cylinders, displacement, horsepower, weight, acceleration]

    # Method 2:  Obtain form inputs and add to numpy array   
    features = [float(x) for x in request.form.values()]
    
    # convert list to numpy array (all values must be numerical for prediction to work)
    final_features = [np.array(features)]

    # use form results to make prediction
    prediction = model.predict(final_features)[0]

    # create html content - either single variable, dictionary, or string
    prediction_text = f"The predicted miles per gallon based on the inputs are {round(prediction,1)} mpg."

    # send prediction to html page
    return render_template("index.html", result = prediction_text)


if __name__ == "__main__":
    app.run()
