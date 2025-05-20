import os

API_ID = API_ID = 25967358

API_HASH = os.environ.get("API_HASH", "10a5a31171dfdc323efdbcf84a8fb016")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8151035412:AAGnfaXf0-gUKtVdaPU-kUZC-VcPaJC0AA8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7733608738))

LOG = -1002452084505

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7733608738").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


