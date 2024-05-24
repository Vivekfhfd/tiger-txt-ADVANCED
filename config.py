import os

API_ID = API_ID = 7273627

API_HASH = os.environ.get("API_HASH", "ee9172964fda7050eed58701c7ff8917")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7064581993:AAF5oIlE_8vPjQ1Gc1_YusrQeNnlop6sXvE")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1833865556))

LOG = -1002106094933

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1833865556").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


