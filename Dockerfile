# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /C:/Users/evgenyp/Desktop/Assets/Cellenium/tests/google/test_dummy.py

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME Cellenium

# Run tests when the container launches
CMD ["python", "./tests/google/test_dummy.py"]
