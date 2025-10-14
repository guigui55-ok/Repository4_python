#!/home/xs023733/anaconda3/bin/python
# encoding: utf-8
import sys, os
sys.path.append("/home/xs023733/necko562.com/public_html/test_project1/")
os.environ['DJANGO_SETTINGS_MODULE'] = "test_project1.settings"
from wsgiref.handlers import CGIHandler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
CGIHandler().run(application)