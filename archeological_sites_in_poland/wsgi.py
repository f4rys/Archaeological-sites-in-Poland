import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archeological_sites_in_poland.settings')

application = get_wsgi_application()
