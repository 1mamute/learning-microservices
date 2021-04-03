# python-products-api
Repository to learn microservices.  
This is a simple Python Flask API that returns data from a JSON file (imagine its a DB).  

The products.json file provides a dump of data for ease of use (instead of settings a local DB).  

References lessons:  
https://www.youtube.com/watch?v=n0rPo2LVmhI&list=WL&index=31&t=3053s  
https://www.youtube.com/watch?v=qbLc5a9jdXo&t=2388s


Build the image  
`sudo docker build . -t python-products-api:latest`

Run the container  
`sudo docker run --rm --name flask --env-file=.env --network=host python-products-api:latest`