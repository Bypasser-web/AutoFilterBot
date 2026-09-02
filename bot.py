import re
import os
from os import environ

id_pattern = re.compile(r'^-\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_Search')
API_ID = int(environ.get('API_ID', '23209524'))
API_HASH = environ.get('API_HASH', '3042159268b8b90557a5e2b8ab346843')
BOT_TOKEN = environ.get('BOT_TOKEN', '8682355615:AAFz59jqODW647mM7oIFMTI0IKuF_mRTBLs')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://graph.org/file/9e9634b62c14156c7c6a2-6628f9a76931e17c5b.jpg')).split()

# Admins & Channels
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', 'Vinay_yadav_166').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1003963697690').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001998334471')
auth_grp = environ.get('AUTH_GROUP', '-1002186753065')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else []

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://vinaykumaryadav1666:e4UWph0YRTo4srxM@cluster0.r8elc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1003963697690))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'telugumovies40')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>{file_name}</b>\n\n<b>Join: @telugumovies40</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b>\n\n🎬 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: {year}\n🌟 Rating: {rating} / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1003963697690')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
