# Use the official Python image as a base image
FROM python:latest

# Install required packages
RUN pip install selenium
RUN pip install python-dotenv

# Set the working directory
# WORKDIR /scripts

# Copy Selenium scripts into the container
COPY /scripts ./

# Make bash run script executable
RUN chmod +x run.sh

# Execute script
CMD ["./run.sh"]