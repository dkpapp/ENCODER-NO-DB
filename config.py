import os
import dotenv
#import SmartEncoder.Database.db.myDB as db


dotenv.load_dotenv()

class Config(object):
  API_ID = int(os.environ.get("API_ID", 12345))
  API_HASH = os.environ.get("API_HASH")
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  AUTH_USERS = os.environ.get("AUTH_USERS")
  GOD = os.environ.get("GOD")
  REDIS_HOST = os.environ.get("REDIS_HOST")
 # REDIS_PORT = int(os.environ.get("REDIS_PORT", 12345))
  REDIS_PASS = os.environ.get("REDIS_PASS")
  DOWNLOAD_LOCATION = "downloads"

Config.AUTH_USERS = [5585763218]
Config.API_ID = 3281305
Config.API_HASH = "a9e62ec83fe3c22379e3e19195c8b3f6"
Config.BOT_TOKEN = "6229797023:AAEZue90zF2D7M573-09sn6XetjJixP1UPE"
Config.REDIS_HOST = "redis-18035.c270.us-east-1-3.ec2.cloud.redislabs.com" 
#redis-14044.c91.us-east-1-3.ec2.cloud.redislabs.com
Config.REDIS_PASS = "5E7W4uBrih6o2x75PJcbM68KI7Tls4re"
#FEsHndW4SHTzcTJQWJYHpCDja6RmYnhf
REDIS_PORT = "18035"
#14044
#.

#.
