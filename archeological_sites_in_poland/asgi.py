import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'archeological_sites_in_poland.settings')

application = get_asgi_application()
