# Use the official Python image as a base image
FROM python:latest

## Getting Chrome and ChromeDriver ##
RUN curl https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chromedriver-linux64.zip -O && \
    unzip chromedriver-linux64.zip


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