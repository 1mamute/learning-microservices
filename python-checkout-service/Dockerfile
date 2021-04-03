FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]