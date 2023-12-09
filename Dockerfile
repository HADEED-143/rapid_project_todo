# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install project dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Django project code into the container
COPY . /app/

# Expose the port that Django will run on
EXPOSE 8000

# Command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
