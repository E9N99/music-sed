from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/d7f33299ed8c60ad82721.mp4")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/27f3254f92a6d4f2a9864.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tipthon_help")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/E9N99")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1488114134").split()))


FAILED = "https://graph.org/file/a7a4ba8ac40b7f0bfb46f.jpg"
