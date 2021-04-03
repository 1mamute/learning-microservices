FROM python:3

ENV FLASK_APP=$FLASK_APP
ENV FLASK_ENV=$FLASK_ENV

WORKDIR /usr/src/app

COPY . .

RUN python3 -m pip install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

CMD ["flask", "run"]