from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.json_util import dumps
import json

myclient = MongoClient("mongodb://root:example@mongodb:27017/")
mydb = myclient["local"]
mycol = mydb["products"]

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello from Python Products Service!'


@app.route('/products')
def get_products():
  products = mycol.find()
  list_cur = list(products)
  return dumps(list_cur, indent=4)


@app.route('/product/<uuid>')
def get_product(uuid):
  product = mycol.find_one({"_id": uuid})
  return dumps(product, indent=4)