** Under Construction **

# heroku-django-docker-example
The smallest "reasonable" project for running a Django project under Heroku Docker

There are a few examples of how to run Python programs in Docker, but there is not a complete example
that brings together a lot of practical considerations.  This is my attempt to rectify that.

# 1. Running Your Gunicorn Server

Don't forget to collectstatic!

# 2. Using Django-RQ with Workers

* Create a base Dockerfile, then a bunch of service-specific Dockerfiles

# 3. Handling Environment Variables

