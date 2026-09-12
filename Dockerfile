FROM python:3.14-slim

workdir /app

Copy /backend/requirements.txt .

run pip install -r requirements.txt

copy /backend/app.py .

expose 5000

cmd ["python","app.py"]

 

