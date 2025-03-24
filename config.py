import os

class Config:
    API_ID = os.environ.get("API_ID", "23294809")
    API_HASH = os.environ.get("API_HASH", "fbe5152195458e6aa8ec4298c96fb274")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7545122233:AAGlDCqGFJJRL75T8UYXERUQlMwzAgkBb3A") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://sagnikgraviton847:AutoForward@autoforward.iwsux.mongodb.net/?retryWrites=true&w=majority&appName=AutoForward")
    DB_NAME = os.environ.get("DB_NAME", "AutoForward")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '1226915127').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    







    
    
    
    
    
    # Jishu Developer 
