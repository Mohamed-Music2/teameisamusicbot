## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAAokFYkNkouh3MyD9WJzi6L-J5Kh_p1qRCj5KUluNf4Dvcl8YniPxTvqyCgeGKLQcAZSTxIC_ixRHwoDsls3IX4iDwR4y2OAhvdYJvFO6w4OyRunLg4R5hEH0AWzTFe_SLSdqNOIcB7YnbPebTljrCi4-YNm99oU9OGuqt_glN74Xz2J1EFWVXdx5rehErxH3WprgwhZjXWyqh-IiaZoWION15eSfScfhtTlsVOPaHh9lpPAriVDsd5i8Ktq3kyfjMpP1bJZAVbf1jG9H1j2RUV8YiTLaEITPxQvusecD5xPOOOa9VZAaq5YVjdZgo80khY5S5SbSsf94_QK3rJ9jNJAAAAAS2FcekA")
BOT_TOKEN = getenv("BOT_TOKEN", "5409818512:AAHNVmbdbgAV_NBWmRl3cpU7Wpp2rWDzpz4")
BOT_NAME = getenv("BOT_NAME", "- 𝚃𝙰𝙴𝙼 𝙴𝙸𝚂𝙰 𝙼𝚄𝚂𝙸𝙲 ‹𝟹 .")
API_ID = int(getenv("API_ID", "16050450"))
API_HASH = getenv("API_HASH", "0dd89e225b6ddd6f03e8135460d31177")
OWNER_NAME = getenv("OWNER_NAME", "🇩🇪ؖؖؖؖؖؖؖؖؖؖ𓆩『𖤍𝑬𝑰𝑺𝑨㉨』𝑴𝑶𝑯𝑨𝑴𝑬𝑫𓆪ؖؖؖؖؖؖؖؖؖ✹ ⃝⃙𓆩™")
OWNER_USERNAME = getenv("OWNER_USERNAME", "lMl4ll")
ALIVE_NAME = getenv("ALIVE_NAME", "- 𝚃𝙰𝙴𝙼 𝙴𝙸𝚂𝙰 𝙼𝚄𝚂𝙸𝙲 ‹𝟹 .")
BOT_USERNAME = getenv("BOT_USERNAME", "lMl4ll_MUSIC_BOT")
OWNER_ID = getenv("OWNER_ID", "5191100896")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "- 𝚃𝙰𝙴𝙼 𝙴𝙸𝚂𝙰 𝙼𝚄𝚂𝙸𝙲 ‹𝟹 .")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BarEisa")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "D_o_m_A12")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5191100896").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "25"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
