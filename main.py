from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from passlib.hash import sha256_crypt

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/"
client = MongoClient("mongodb://localhost:27017")
db = client["Hostel Compliants"]  # Replace with your database name

@app.route('/')
def display_info():
    # Retrieve contact data from MongoDB
    info_collection = db.info #variable = database.collectionname
    info_11 = info_collection.find() # query to find and storing in variable
    return render_template('1_CompliantForm.html', info_22=info_11)

@app.route('/2_Status')
def display_prep_mat():
    # Retrieve contact data from MongoDB
    prepmat_collection = db.Preparation_Material #database.collectionname
    prepmat_11 = prepmat_collection.find()
    return render_template('Status.html', prepmat_22=prepmat_11)

@app.route('/3_Login')
def display_courses():
    # Retrieve contact data from MongoDB
    courses_collection = db.courses #database.collectionname
    courses_11 =  courses_collection.find()
    return render_template('Login.html', courses_22=courses_11)



app.run(debug=True)