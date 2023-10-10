import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)

db = client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/show", methods=["POST"])
def show_post():
        name_receive = request.form['name_give']
        address_receive = request.form['address_give']
        acres_receive = request.form['acres_give']
        doc = {
            'name' : name_receive,
            'address':address_receive, 
            'acres':acres_receive 
        }
        db.Mars.insert_one(doc)
        return jsonify({'msg':'POST request'})

@app.route("/show", methods=['GET'])
def show_get():
      buyer_list = list(db.Mars.find({},{'_id':False}))
      return jsonify({'messages' : buyer_list})

if __name__ == '__main__' :
      app.run('0.0.0.0', port=5000, debug=True)
