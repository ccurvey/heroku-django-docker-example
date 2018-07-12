#############################################################################
#Grab the latest OS image
FROM heroku/heroku:16

#############################################################################
# install python and pip
RUN apt-get update
RUN apt-get install -y \
  python \
  python-pip

#############################################################################
## Encoding
RUN locale-gen en_US.UTF-8

#############################################################################
# Install dependencies.  Upgrade pip, then install numpy before adding the
# rest of our requirements.
RUN pip install --upgrade pip
RUN pip install numpy

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

##############################################################################
# create a directory for our code
RUN mkdir -p /opt/webapp
WORKDIR /opt/webapp

############################################################################
# Set up a non-root user, per Heroku's instructions, and change ownership of
# our app directory to that user
RUN useradd -m myuser

######################################
# Expose is NOT supported by Heroku.  During local testing, you can use
#
#   docker run -p 8000:8000 -e PORT=8000 <tag>:latest
#
######################################
# EXPOSE 8000

##############################################################################
# we do not run the app in this file. That comes in the files that extend
# this Dockerfile.
##############################################################################
