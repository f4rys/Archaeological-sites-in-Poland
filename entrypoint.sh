#!/bin/sh

# Use secrets from environment variables
export SECRET_KEY=${SECRET_KEY}
export DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}
# ... (add other secrets as needed)

# Start Gunicorn 
exec gunicorn archeological_sites_in_poland.wsgi:application
