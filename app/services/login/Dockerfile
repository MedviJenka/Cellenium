FROM python:3.11-slim-buster
WORKDIR /login
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 1000
CMD ["python", "app.py"]
