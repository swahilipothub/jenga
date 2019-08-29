from jenga.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jenga',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True

SECRET_KEY = "K5VYabpdUqVAmSuVeQVQj/5EI1RDvfOJyvAR7qMkkbo="

# obtain this from africastalking's website
AFRICASTALKING_USERNAME = "swahilipothub"
AFRICASTALKING_APIKEY = "bb4f496e9865eac6d632fa567a0fa90a96a1e013320a97f8874c1ba7950b665a"
AFRICASTALKING_SENDER = "Swahilipot"

# Email Backend settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
