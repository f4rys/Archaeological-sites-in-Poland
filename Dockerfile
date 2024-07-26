# Base Image: Python 3.12.4
FROM python:3.12.4-slim-bullseye

# Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY=DUMMY_SECRET
ENV DJANGO_SETTINGS_MODULE=archeological_sites_in_poland.dev_settings

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project code into the container
COPY . /app/

# Collect static files and prepare database
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
RUN python manage.py load_data

# Expose the port
EXPOSE 8000

# Entrypoint Script for Managing Secrets
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Start the application using the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
