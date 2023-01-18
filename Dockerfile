FROM python:3.7.2-stretch

# Set the working directory to /AppPython
WORKDIR /house_rent

# Copy requirements.txt file in current folder into the container at /AppPython 
ADD requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Jupyter listens port:
EXPOSE 5000:128
