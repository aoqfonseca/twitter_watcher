import os


class Config(object):

    DEBUG = os.environ.get('API_DEBUG', 0) in ('true', 'True', '1')
    MONGODB_SETTINGS = {
        'DB': os.environ.get('MONGODB_URL', 'twitter_watcher')
    }

    APP_TWIITER_ID = os.environ.get('APP_TWIITER_ID')
    APP_TWIITER_SECRET = os.environ.get('APP_TWIITER_SECRET')
    TOKEN_TWIITER_ID = os.environ.get('TOKEN_TWIITER_ID')
    TOKEN_TWIITER_SECRET = os.environ.get('TOKEN_TWIITER_SECRET')
    SECRET_KEY = 'KeepThisS3cr3t3'
    BROKER_URL = os.environ.get('CELERY_BROKER_URL',
                                'redis://localhost:6379/0')
