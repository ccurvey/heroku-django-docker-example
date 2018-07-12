**Under Construction**

# heroku-django-docker-example
The smallest "reasonable" project for running a Django project under Heroku
Docker

There are a few examples of how to run Python programs in Docker, but there is
not a complete example that brings together a lot of practical considerations.
This is my attempt to rectify that.

I have tried to add comments liberally throughout the code.

# Project Overview

When building a Python project in Heroku, Heroku has some (strong) suggestions
about how to handle different use-cases.

 * Security credentials in environment variables
 * Django for web-serving
 * dj_database_url for converting the DATABASE_URL to a Django database
   configuration
 * Django-RQ for dealing with background tasks
 * WhiteNoise for serving static assets (images, CSS, etc)

I will try to illustrate all of those.

In addition, you probably found this example because you were trying to figure
out how to use Numpy, Scipy, Pandas, etc with Heroku.  So I'll add that just
for fun.

Note:  This app depends on Redis (for Django-RQ) and Postgres, and I'm assuming
that you are running them as "normal" processes on localhost, and not trying
to run them within a Docker container.

# Docker Setup and Use

## Dockerfile Structure

We have a base Dockerfile that prepares an image for us. Then we have a series
of related Dockerfiles (Dockerfile.web, Dockerfile.background1,
Dockerfile.background2) that inherit from the base Dockerfile.

## Building Docker Images

### Base Image

To build the base image, do:

    $ docker build --tag example --file Dockerfile .

Note that the use of "example" as a tag is important -- it is referenced in the
"FROM" lines of the other Dockerfiles

### Other Images

To build a specific image:

   $ docker build --tag example/web --file Dockerfile.web .

(replace "web" with the specfic file you want)

## If I Change "X", What Do I Have to Rebuild?

* If you add something to the operating system (e.g. "apt-get install"), add
  that to your Dockerfile (near line 8), and rebuild the base image
* If you add something to your virtualenv (e.g. "pip install"), add that
  to your requirements.txt, and rebuild the base image
* If you change Python code, rebuild the image you are working on

# Running Individual Containers

## The Web Process

You have to specify the ports to get everything tied together

    $ docker run -p 8000:8000 -e PORT=8000 example/web

## Worker Processes

    $ docker run example/larry  (or curly, or moe)

* Create a base Dockerfile, then a bunch of service-specific Dockerfiles

# Running Everything with Docker-Compose


# Environment Variables
