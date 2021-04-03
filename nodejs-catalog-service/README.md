# nodejs-catalog-service
Repository to learn microservices.  
This is a simple nodejs service that lists data from a REST API (in this case https://github.com/1mamute/python-products-api).  

References lessons:  
https://www.youtube.com/watch?v=n0rPo2LVmhI&list=WL&index=31&t=3053s  

Build the image  
`sudo docker build . -t nodejs-catalog-service:latest`

Run the container  
`sudo docker run --rm --name node --env-file=.env --network=host nodejs-catalog-service:latest`