FROM rabbitmq:latest

RUN echo $(grep $(hostname) /etc/hosts | cut -f1) rabbitmq-queue >> /etc/hosts