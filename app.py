# Dependencies
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
import json
import numpy as np
import pandas as pd
#######################################################################
## Database Setup
#######################################################################
#engine = create_engine("sqlite:///hospital.sqlite")

#reflect an existing database into a new model
#Base = automap_base()

# reflect the tables
#Base.prepare(engine, reflect=True)

#Save Reference to the table
#Hospital = Base.classes.hospital

##################################################################
# Flask Setup
##################################################################
app = Flask(__name__)


@app.route("/")
#define what to do when user hits the index route
def welcome():
    return render_template('index_HP2.html')


# @app.route("/datatable")
# #define what to do when user hits the index route
# def datatable():
#     return render_template('index_datatable1.html')


@app.route("/api/v1.0/hospital_information")
def hospital_information():
    with open("hospital_data_final.csv") as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            print(row)
     


# @app.route("/api/v1.0/hospital_locations")
# def hospital_locations():
#     with open("il_hospital_coord_rev.csv") as file:
#         file_reader = csv.reader(file)
#         for row in file_reader:
#             print(row)

# -- hospital list 
df = pd.read_csv("hospital_data_cleanv.csv")
df.to_csv("hospital_data_cleanv.csv", index=None)
  
# route to html page - "table"
@app.route('/datatable')
def csvtohtml():
    
    # converting csv to html
    data = pd.read_csv("hospital_data_cleanv.csv")
    return render_template("index_datatable1.html", tables=[data.to_html(index=False)], titles=[''])
  
if __name__ == "__main__":
    app.run(debug = True)


# #@app.route("/api/v1.0/staffed_beds")
# #def staffed_beds():
#     #create session link
#  #   session = Session(engine)
#     #return list of staffed bed data for each hospital
#   #  results = session.query(Hospital.hospitalNames, Hospital.staffedBeds).all()

#     session.close()

#     all_hospitals = []
#     for hospitalNames, staffedBeds in results:
#         hospital_dict = {}
#         hospital_dict = ["Name"] = hospitalNames
#         hospital_dict = ["Staffed Beds"] = staffedBeds
#         all_hospitals.append(hospital_dict)
    
#     return jsonify(all_hospitals)

@app.route("/api/v1.0/staffed_beds")
def staffed_beds():
    with open("./visualizations/plots_beds.js") as file:
        js_decoded = js.load(file)

    return js_decoded

# @app.route("/api/v1.0/top20")
# def top20():
#     #create session link
#     session = Session(engine)
#     #return list of staffed bed data for each hospital
#     results = session.query(Hospital.hospitalNames, Hospital.googleStars).all()

#     session.close()

#     top_ratings = []
#     for hospitalNames, googleStars in results:
#         ratings_dict = {}
#         ratings_dict = ["Name"] = hospitalNames
#         ratings_dict = ["Google Stars"] = googleStars
#         top_ratings.append(ratings_dict)
    
#     return jsonify(top_ratings)

@app.route("/api/v1.0/top20")
def top20():
    with open("./visualizations/plots_top20.js") as file:
        js_decoded = js.load(file)

    return js_decoded


# @app.route("/api/v1.0/bottom20")
# def bottom20():
#     #create session link
#     session = Session(engine)
#     #return list of staffed bed data for each hospital
#     results = session.query(Hospital.hospitalNames, Hospital.googleStars).all()

#     session.close()

#     bottom_ratings = []
#     for hospitalNames, googleStars in results:
#         bottom_dict = {}
#         bottom_dict = ["Name"] = hospitalNames
#         bottom_dict = ["Google Stars"] = googleStars
#         bottom_ratings.append(bottom_dict)
    
#     return jsonify(bottom_ratings)

@app.route("/api/v1.0/bottom20")
def bottom20():
    with open("./visualizations/plots_bottom20.js") as file:
        js_decoded = js.load(file)

    return js_decoded



if __name__ == '__main__':
    app.run(debug = True)      




