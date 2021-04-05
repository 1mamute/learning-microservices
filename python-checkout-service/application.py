from flask import Flask
from dotenv import load_dotenv
import json
import os
import requests

dir_path = os.path.dirname(os.path.realpath(__file__))

load_dotenv()

app = Flask(__name__)

products_url = "http://127.0.0.1:8002"


@app.route('/')
def index():
  return 'Hello from Python Checkout Service!'


@app.route('/<uuid>')
def display_checkout(uuid):
  products_endpoint = products_url + "/product/" + uuid
  print(products_endpoint)
  response = requests.get(products_endpoint)
  print(response.status_code)
  print(response.content)
  return 'Product uuid: ' + uuid
