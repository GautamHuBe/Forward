# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", 20747302)
    API_HASH = environ.get("API_HASH", "6e086ad99a197709af10425d7c7c1b65")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6805001741').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "forward") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://diliya:diliya@cluster0.umeyupr.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Forward")

    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002096968650'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "GKBOTZ") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    NAME = None
    UNAME = None
    ID = None
