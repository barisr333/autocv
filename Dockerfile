# Use the official Python image as a base image
FROM python:3.9.18-slim-bullseye

## Getting Chrome and ChromeDriver ##

RUN apt-get update && apt-get install -y wget

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update && apt-get install -y google-chrome-stable


# Install required packages
RUN pip install selenium
RUN pip install python-dotenv

# Copy Selenium scripts into the container
COPY /scripts ./
COPY .env .

# Make bash run script executable
RUN chmod +x run.sh

# Execute script
CMD ["./run.sh"]