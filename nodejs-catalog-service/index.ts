import express from 'express';
import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config({ path: __dirname + '/.env' });

const app = express();
const PORT = process.env.PORT;
const PRODUCTS_URL = 'http://127.0.0.1:5000'

app.get('/', (req, res) => res.send('Hello from Node Catalog Service!'));

app.get('/products', (req, res) => {
  axios.get(PRODUCTS_URL + "/products")
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error);
    });
});

app.listen(PORT, () => {
  console.log(`⚡️[server]: Server is running at http://127.0.0.1:${PORT}`);
});