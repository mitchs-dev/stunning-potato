# We are using 'python:3.9.10' for our base image
FROM python:3.9.10

# This sets our working directory for the image
WORKDIR /usr/src/app

# Next we need to copy our `.py` file  to our image
COPY session6.py .

# Now we set our  command
CMD [ "python", "./session6.py" ]