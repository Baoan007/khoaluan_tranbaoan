import os
from dotenv import load_dotenv
load_dotenv()
# Configuration for Flask app

# Mặc định là production


class Config(object):
    DEBUG = os.getenv('DEBUG') == "dev"
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(32)
    DOMAIN = os.getenv('DOMAIN')
    RASA_ENABLE = True


# Configuration for Firebase Cloud Messaging


class FCMConfig(object):
    pass


# Môi trường cho dev
class DevConfig(Config):
    DEBUG = True
    DOMAIN = "http://127.0.0.1:8000"


class DevFCMConfig(FCMConfig):
    pass


# Set Flask environment based on FLASK_ENV variable
if os.getenv('DEBUG') == 'prod':
    app_config = Config()
    fcm_config = FCMConfig()
else:
    app_config = DevConfig()
    fcm_config = DevFCMConfig()
