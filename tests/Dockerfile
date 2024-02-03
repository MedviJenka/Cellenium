ARG PYTHON=3.8-slim
FROM python:${PYTHON} as build
WORKDIR /tests
COPY . /tests
RUN pip install --upgrade pip && run pip install --no-cache-dir --compile -r requirements.txt
