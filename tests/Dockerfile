FROM python:3.8 as build
WORKDIR /tests/
COPY requirements.txt .
COPY . .
RUN pip install --upgrade pip && run pip install -r requirements.txt
