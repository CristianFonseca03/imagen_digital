from imagen_digital.settings.base import *
import django_heroku
django_heroku.settings(locals())

DEBUG = True