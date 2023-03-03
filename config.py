
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

Config.AUTH_USERS = [2067727305, 5596561127]
Config.API_ID = 14604313
Config.API_HASH = "a8ee65e5057b3f05cf9f28b71667203a"
Config.BOT_TOKEN = "5311193187:AAH2HYm39hNoumWsmnZ4SO3ZoStNYsvps9A"
Config.REDIS_HOST = "redis-10344.c275.us-east-1-4.ec2.cloud.redislabs.com"
Config.REDIS_PASS = "2bdmUMBhHt1q7dalbm3MnKbOmWFMsgaP"
REDIS_PORT = "10344"
