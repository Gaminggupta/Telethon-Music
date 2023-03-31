import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6130581603:AAGumi9Svad97kk_3R_sRIaHvmIjA2BYR7w)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOLwBu1IgjWFfmmA-e7cmGVmOkF0p7wGbLVFdqxNcRLTzxvIXAGUR5EpngFGvwU08UA6SGIUzXFipgqgdize97kg_B6oqQc6RKMDYTRlPVNlTmlJHyeXv1DClb4u1fvDkUaVm5InmUduuERwx7AwOUf8DEJ8VosYNhhZYR9FRgCONRMRgwKBXDaVWGlt4cU5r8AgGhlOUmA3RVabz7E2fCm_1ZEyDfiCKX4PWIxpVJlrls3QGaX92pnZYxwYxL6aQcYT5ZswM9n1-RltXI0IUrST0V9GBkvIpGRVJVkzcUYIn60dAvEbrsNxixM2eAXXnBGdvlkpzxK4OKEGrc9Eq_gQcgZ8=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
