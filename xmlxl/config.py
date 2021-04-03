import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Generating Secret Key:
# It is a key that is used to protect against CSRF (Cross-Site Request Forgery)
# It is important to keep the key secret - accessible only to limited operations and maintenance personnel
# Use "secrets" library to generate the key:
# import secrets
# SECRET_KEY = secrets.token_urlsafe(64)
#
# IMP:  The secret key should ideally be loaded from environment variable. 
#       However, during development, it is okay to use hard-coded string as shown below

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'LTnW_Jlck84n6NQ6Mzbm3_VK372WLNnhqJfttxe076A'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'xmlxl.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Limiting file upload size to 5 MB
    MAX_CONTENT_LENGTH = 1024 * 1024 * 5
    
    # Config Settings for Celery
    # CELERY_BROKER_URL = 'amqp://celery:Local99@localhost:5672/celery_vhost'
    CELERY_BROKER_URL = 'amqp://celery:Local99@127.0.0.1:5672/celery_vhost'
    CELERY_RESULT_BACKEND = 'rpc://'

