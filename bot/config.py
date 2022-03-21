

import os
from dotenv import load_dotenv
from bot.translation import Translation

# apparently, no error appears even if the path does not exists
load_dotenv("config.env")


class Config:
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
    # required for running on Heroku
    URL = os.environ.get("URL", "")
    PORT = int(os.environ.get("PORT", 5000))
    # Python3 ReQuests CHUNK SIZE
    CHUNK_SIZE = 10280
    # MyTelegram.org
    # configurtion required while creating new application
    APP_TITLE = os.environ.get("APP_TITLE", "TGScrapAPID")
    APP_SHORT_NAME = os.environ.get("APP_SHORT_NAME", "TGScrapAPID")
    APP_URL = os.environ.get("APP_URL", "https://telegram.dog/TGScrapAPIDbot")
    # these platform informations were obtained
    # on 27.01.2020 21:15:50 IST
    APP_PLATFORM = [
        "android",
        "ios",
        "wp",
        "bb",
        "desktop",
        "web",
        "ubp",
        "other"
    ]
    # if any of the platform, does not work
    # please reopen
    # https://github.com/SpEcHiDe/MyTelegramOrgRoBot/issues/3
    APP_DESCRIPTION = os.environ.get(
        "APP_DESCRIPTION",
        "created using https://telegram.dog/TGScrapAPIDbot"
    )
    #
    FOOTER_TEXT = os.environ.get("FTEXT", "❤️ @buzzsupport")
    # the strings used in the different messages
    # in the bot
    START_TEXT = os.environ.get("START_TEXT", Translation.START_TEXT)
    AFTER_RECVD_CODE_TEXT = os.environ.get(
        "AFTER_RECVD_CODE_TEXT",
        Translation.AFTER_RECVD_CODE_TEXT
    )
    BEFORE_SUCC_LOGIN = os.environ.get(
        "BEFORE_SUCC_LOGIN",
        Translation.BEFORE_SUCC_LOGIN
    )
    ERRED_PAGE = os.environ.get("ERRED_PAGE", Translation.ERRED_PAGE)
    CANCELLED_MESG = os.environ.get(
        "CANCELLED_MESG",
        Translation.CANCELLED_MESG
    )
    IN_VALID_CODE_PVDED = os.environ.get(
        "IN_VALID_CODE_PVDED",
        Translation.IN_VALID_CODE_PVDED
    )
    IN_VALID_PHNO_PVDED = os.environ.get(
        "IN_VALID_PHNO_PVDED",
        Translation.IN_VALID_PHNO_PVDED
    )
