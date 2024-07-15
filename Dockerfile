# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY ./core /app

# Ensure that the path includes the directory where Celery and other Python scripts are installed
ENV PATH="/root/.local/bin:$PATH"

# Expose the port the app runs on
EXPOSE 8000

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
