from flask import Flask
from dotenv import load_dotenv
import os
import requests

dir_path = os.path.dirname(os.path.realpath(__file__))

load_dotenv()

app = Flask(__name__)

products_url = "python-products-service:8002"


@app.route('/')
def index():
  return 'Hello from Python Checkout Service!'


@app.route('/products')
def display_all_checkout():
  response = requests.get(products_url + "/products")
  print(response.status_code)
  return response.content


@app.route('/product/<uuid>')
def display_checkout(uuid):
  response = requests.get(products_url + "/product/" + uuid)
  print(response.status_code)
  print(response.content)
  return 'Product uuid: ' + uuid