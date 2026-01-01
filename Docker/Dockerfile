# Pull the base image from registry
# Base image provides starting OS, pre-built env and tools your container begins with

FROM python:3.11-slim

# Sets the current folder inside conainer to /python
# We wil be inside "/python" folder

WORKDIR /python

# apt-get update: Package manager for debian
# Fetches list of latest available packages from ubuntu server

# apt-get install: installs the requested packages
# These system level packages are installed as base images do not include these

RUN apt-get update -y && apt-get install -y \
    curl \
    wget \
    build-essential \
    libpq-dev


# Copy the requirements.txt /all folders from our directory to containers workdir

COPY requirements.txt .
COPY . . 

# Install the different python libraries required
RUN pip install -r requirements.txt

# Create a directory '/notebooks' inside the /python to store the notebook files 
RUN mkdir -p /python/notebooks

# Launch the jupyter notebook (command below) once we run the the created image

CMD jupyter notebook --no-browser --allow-root --ip 0.0.0.0

# While creating an image, make sure to forward port and create volume
# docker run -p 8888:8888 -v ./jupyter_data:/python/notebooks image_name
# We are forwarding local host's port 8888 to container's 8888

# Volume created on host side at ./jupyter_data and on container side at /python/notebooks
# This is a bind mount

# Other example can be to run a .py file once the container starts
# CMD ["python", "check.py"]



