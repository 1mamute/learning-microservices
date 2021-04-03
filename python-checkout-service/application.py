from flask import Flask
from dotenv import load_dotenv
import json
import os
import requests

dir_path = os.path.dirname(os.path.realpath(__file__))

load_dotenv()

app = Flask(__name__)

products_url = os.getenv("PRODUCTS_URL")


@app.route('/')
def index():
  return 'Hello from Python Checkout Service!'


@app.route('/products')
def get_products():
  with open(dir_path + '/' + 'products.json') as json_file:
    data = json.load(json_file)
    return json.dumps(data, indent=4)


@app.route('/<uuid>')
def display_checkout(uuid):
  response = requests.get(products_url + "/product" + uuid)
  print(response.status_code)
  print(response.content)
  return 'Product uuid: ' + uuid
