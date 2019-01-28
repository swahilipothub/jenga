from jenga.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jenga',
        'USER': 'jenga_user',
        'PASSWORD': 'jurn3hkfkkd',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True

SECRET_KEY = "K5VYabpdUqVAmSuVeQVQj/5EI1RDvfOJyvAR7qMkkbo="

# obtain this from africastalking's website
AFRICASTALKING_USERNAME = "swahilipothub"
AFRICASTALKING_APIKEY = "649730e2d5cf9abade5872894c53ef9c8367a765ad505710c594599c9ed5a984"

# Email Backend settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
