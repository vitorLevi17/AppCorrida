# This file contains the WSGI configuration required to serve up your
# Django app
import os
import sys

# Add your project directory to the sys.path
settings_path = '/home/AppCorridas/appcorridas.pythonanywhere.com/AppCorridas'
sys.path.insert(0, settings_path)

# Set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'setup.settings'

# Set the 'application' variable to the Django wsgi app
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
