from flask import Flask
from dotenv import load_dotenv
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello!'


@app.route('/products')
def get_products():
  with open(dir_path + '/' + 'products.json') as json_file:
    data = json.load(json_file)
    return json.dumps(data, indent=4)


@app.route('/product/<uuid>')
def get_product(uuid):
  with open(dir_path + '/' + 'products.json') as json_file:
    data = json.load(json_file)
    product = data['products'][0]
    return json.dumps(product, indent=4)
