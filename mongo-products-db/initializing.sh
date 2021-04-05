#!/bin/bash

mongoimport --db local --collection products --authenticationDatabase admin --username root --password example --drop --file /docker-entrypoint-initdb.d/products.json
