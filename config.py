
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "20747302")
    API_HASH = environ.get("API_HASH", "6e086ad99a197709af10425d7c7c1b65")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8099582490:AAH7Asj9XB4JdqYdRdlcSFQz_rhtqkJDsXs") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6805001741').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "forward") 

    PICS = (environ.get('PICS', 'https://envs.sh/s/0jAf2Ta5kVg5AdnqZj-vIQ/Snp.png'))
    
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://diliya:diliya@cluster0.umeyupr.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Forward")

    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002096968650'))
    FSUB_CHANNELS = environ.get('FSUB_CHANNEL', [-1002097024150])


class temp(object): 
    lock = {}
    CANCEL = {}
    CONFIGS = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    NAME = None
    UNAME = None
    ID = None
    
