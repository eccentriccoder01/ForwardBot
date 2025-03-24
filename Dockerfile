# Use Python 3.8 Slim Buster as base image
FROM python:3.8-slim-buster

# Update system packages and install necessary dependencies
RUN apt update && apt upgrade -y && apt install -y git

# Copy and install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

# Set working directory
WORKDIR /bot

# Copy necessary files
COPY . /bot
RUN chmod +x start.sh

# Run the startup script
CMD ["/bin/bash", "/start.sh"]
