from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text
from .main import *
from config import ADMIN

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    data = query.data

    if data == "start":
        await query.message.edit_text(
            text.START.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
                 InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help")],
                [InlineKeyboardButton("♻ ᴅᴇᴠᴇʟᴏᴘᴇʀ ♻", user_id=int(ADMIN))]
            ])
        )
    elif data == "help":
        await query.message.edit_text(
            text.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ᴜᴩᴅᴀᴛᴇꜱ", url="https://telegram.me/Techifybots"),
                 InlineKeyboardButton("ꜱᴜᴩᴩᴏʀᴛ", url="https://telegram.me/TechifySupport")],
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                 InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
            ])
        )
    elif data == "about":
        await query.message.edit_text(
            text.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💥 ʀᴇᴘᴏ", url="https://github.com/TechifyBots/Stylish-Font-Bot"),
                 InlineKeyboardButton("👨‍💻 ᴏᴡɴᴇʀ", user_id=int(ADMIN))],
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                 InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
            ])
        )
    elif data == "close":
        await query.message.delete()

    elif query.data == "nxt":
       await nxt_fonts_nxt(client, query)

    elif query.data == "fontblack":
       await style_btn_back(client, query)

    elif "style" in query.data:
       cmd, style = query.data.split('+')
       await style_btn_editz(client, query, style)
