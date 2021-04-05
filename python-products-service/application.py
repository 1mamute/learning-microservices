from flask import Flask
from dotenv import load_dotenv
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello from Python Products Service!'


@app.route('/products')
def get_products():
  with open(dir_path + '/' + 'products.json') as json_file:
    data = json.load(json_file)
    return json.dumps(data, indent=4)


@app.route('/product/<uuid>')
def get_product(uuid):
  with open(dir_path + '/' + 'products.json') as json_file:
    data = json.load(json_file)
    for product in data['products']:
      if (product['uuid'] == uuid):
        return json.dumps(product, indent=4)
      else:
        return "Não encontrado"