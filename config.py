import os

API_ID = API_ID =  29264478

API_HASH = os.environ.get("API_HASH", "9aed4788fce88cb77283abaf0685f469")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6537916708:AAEkgH-tTap6GtoMeM41gtS_RJmEq-ezY2M")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER",5475199171))

LOG = -1002054545048 

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5475199171 5044896938 6116624490 6230767081 5496342413 6347607291 6351476810").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


