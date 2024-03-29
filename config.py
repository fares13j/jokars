import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("7098490366:AAHFbT4QYWX-rcZQo9z0eXJY1MyDCznF1TQ", "")

    APP_ID = int(os.environ.get("APP_ID", 25535561))

    API_HASH = os.environ.get("API_HASH", "f40dbe709ac3d5b8a18aed1edb9b0d04")
