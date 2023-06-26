FROM python:3.11-slim-buster
WORKDIR /image_compare
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "image_compare_executor.py"]
