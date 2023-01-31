# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=18734981, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="0e88a144af021c41897a8e826eaf96aa")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default=1BVtsOL8Bu5pSWCpFVEpOtj0sb7QnoLYgoKFR6ZPvNZ8OjEVkjyctQ5nO3g4gubtOOnjAun1WG2PU15ieh7aRaSo1nn97MEeQcZFpkm-8h_6lFGE_2n8hI7QMNVRojwbSZTHoTaYxxuj9cBcu4hPSNG8JRA986bgdtfEOGJZU0tncUj4XKecpRWX20LDpMSqJubzLdUqUuoFlLXL8nu3a60VQ8xUz4F3eTd5loEG0yXgmOlYa_64q9MGnrlodMhZOol7LzPg_nF6WComDdijwvA2Zop-OUI8pQaPTr4UGOT2gSZeaaqRdsZNsy11VhFPbiow-m33spS3msc_cTsITeM7XT8epvzg=)
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=redis-18203.c241.us-east-1-4.ec2.cloud.redislabs.com:18203) or config("REDIS_URL", default=None))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default=GzqsjNTpugv9DZvKchuQSwrlKevLG4yE)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
