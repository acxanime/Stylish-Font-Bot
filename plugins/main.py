import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .fonts import Fonts

# Map style names to font functions
font_styles = {
    "typewriter": Fonts.typewriter,
    "outline": Fonts.outline,
    "serif": Fonts.serif,
    "bold_cool": Fonts.bold_cool,
    "cool": Fonts.cool,
    "small_cap": Fonts.smallcap,
    "script": Fonts.script,
    "script_bolt": Fonts.bold_script,
    "tiny": Fonts.tiny,
    "comic": Fonts.comic,
    "sans": Fonts.sans,
    "slant_sans": Fonts.slant_san,
    "slant": Fonts.slant,
    "sim": Fonts.sim,
    "circles": Fonts.circles,
    "circle_dark": Fonts.dark_circle,
    "gothic": Fonts.gothic,
    "gothic_bolt": Fonts.bold_gothic,
    "cloud": Fonts.cloud,
    "happy": Fonts.happy,
    "sad": Fonts.sad,
    "special": Fonts.special,
    "squares": Fonts.square,
    "squares_bold": Fonts.dark_square,
    "andalucia": Fonts.andalucia,
    "manga": Fonts.manga,
    "stinky": Fonts.stinky,
    "bubbles": Fonts.bubbles,
    "underline": Fonts.underline,
    "ladybug": Fonts.ladybug,
    "rays": Fonts.rays,
    "birds": Fonts.birds,
    "slash": Fonts.slash,
    "stop": Fonts.stop,
    "skyline": Fonts.skyline,
    "arrows": Fonts.arrows,
    "qvnes": Fonts.rvnes,
    "strike": Fonts.strike,
    "frozen": Fonts.frozen
}

# Font buttons (page 1 and 2)
def get_font_buttons(page=1):
    if page == 1:
        return [[
            InlineKeyboardButton('𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛', callback_data='style+typewriter'),
            InlineKeyboardButton('𝕆𝕦𝕥𝕝𝕚𝕟𝕖', callback_data='style+outline'),
            InlineKeyboardButton('𝐒𝐞𝐫𝐢𝐟', callback_data='style+serif'),
        ],[
            InlineKeyboardButton('𝑺𝒆𝒓𝒊𝒇', callback_data='style+bold_cool'),
            InlineKeyboardButton('𝑆𝑒𝑟𝑖𝑓', callback_data='style+cool'),
            InlineKeyboardButton('Sᴍᴀʟʟ Cᴀᴘs', callback_data='style+small_cap'),
        ],[
            InlineKeyboardButton('𝓈𝒸𝓇𝒾𝓅𝓉', callback_data='style+script'),
            InlineKeyboardButton('𝓼𝓬𝓻𝓲𝓹𝓽', callback_data='style+script_bolt'),
            InlineKeyboardButton('ᵗⁱⁿʸ', callback_data='style+tiny'),
        ],[
            InlineKeyboardButton('ᑕOᗰIᑕ', callback_data='style+comic'),
            InlineKeyboardButton('𝗦𝗮𝗻𝘀', callback_data='style+sans'),
            InlineKeyboardButton('𝙎𝙖𝙣𝙨', callback_data='style+slant_sans'),
        ],[
            InlineKeyboardButton('𝘚𝘢𝘯𝘴', callback_data='style+slant'),
            InlineKeyboardButton('𝖲𝖺𝗇𝗌', callback_data='style+sim'),
            InlineKeyboardButton('Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎', callback_data='style+circles')
        ],[
        InlineKeyboardButton('C͜͡l͜͡o͜͡u͜͡d͜͡s͜͡', callback_data='style+cloud'),
        InlineKeyboardButton('H̆̈ă̈p̆̈p̆̈y̆̈', callback_data='style+happy'),
        InlineKeyboardButton('S̑̈ȃ̈d̑̈', callback_data='style+sad'),
    ],[
    InlineKeyboardButton('🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅢︎', callback_data='style+circle_dark'),
            InlineKeyboardButton('𝔊𝔬𝔱𝔥𝔦𝔠', callback_data='style+gothic'),
            InlineKeyboardButton('𝕲𝖔𝖙𝖍𝖎𝖈', callback_data='style+gothic_bolt'),
        ],[
            InlineKeyboardButton('Next ➡️', callback_data="nxt")
        ]]
    else:
        return [[
            InlineKeyboardButton('🇸 🇵 🇪 🇨 🇮 🇦 🇱 ', callback_data='style+special'),
            InlineKeyboardButton('🅂🅀🅄🄰🅁🄴🅂', callback_data='style+squares'),
            InlineKeyboardButton('🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎', callback_data='style+squares_bold'),
        ],[
            InlineKeyboardButton('ꪖꪀᦔꪖꪶꪊᥴ𝓲ꪖ', callback_data='style+andalucia'),
            InlineKeyboardButton('爪卂几ᘜ卂', callback_data='style+manga'),
            InlineKeyboardButton('S̾t̾i̾n̾k̾y̾', callback_data='style+stinky'),
        ],[
            InlineKeyboardButton('B̥ͦu̥ͦb̥ͦb̥ͦl̥ͦe̥ͦs̥ͦ', callback_data='style+bubbles'),
            InlineKeyboardButton('U͟n͟d͟e͟r͟l͟i͟n͟e͟', callback_data='style+underline'),
            InlineKeyboardButton('꒒ꍏꀷꌩꌃꀎꁅ', callback_data='style+ladybug'),
        ],[
            InlineKeyboardButton('R҉a҉y҉s҉', callback_data='style+rays'),
            InlineKeyboardButton('B҈i҈r҈d҈s҈', callback_data='style+birds'),
            InlineKeyboardButton('S̸l̸a̸s̸h̸', callback_data='style+slash'),
        ],[
            InlineKeyboardButton('s⃠t⃠o⃠p⃠', callback_data='style+stop'),
            InlineKeyboardButton('S̺͆k̺͆y̺͆l̺͆i̺͆n̺͆e̺͆', callback_data='style+skyline'),
            InlineKeyboardButton('A͎r͎r͎o͎w͎s͎', callback_data='style+arrows'),
        ],[
            InlineKeyboardButton('ዪሀክቿነ', callback_data='style+qvnes'),
            InlineKeyboardButton('S̶t̶r̶i̶k̶e̶', callback_data='style+strike'),
            InlineKeyboardButton('F༙r༙o༙z༙e༙n༙', callback_data='style+frozen')
        ],[
            InlineKeyboardButton('⬅️ Back', callback_data='nxt+0')
        ]]

# Handle plain text messages
@Client.on_message(filters.private & filters.text & ~filters.command(["start", "stats", "broadcast"]))
async def send_style_buttons(client, message):
    reply = await message.reply_text(
        message.text,
        reply_markup=InlineKeyboardMarkup(get_font_buttons(1)),
        reply_to_message_id=message.id
    )
    await asyncio.sleep(120)
    await message.delete()
    await reply.delete()

# Pagination handler
@Client.on_callback_query(filters.regex("^nxt"))
async def paginate_buttons(client, callback):
    page = 2 if callback.data == "nxt" else 1
    await callback.answer()
    await callback.message.edit_reply_markup(InlineKeyboardMarkup(get_font_buttons(page)))

# Handle style button click
@Client.on_callback_query(filters.regex("^style"))
async def apply_style(client, callback):
    await callback.answer()
    _, style_name = callback.data.split('+')
    func = font_styles.get(style_name)
    
    if not func:
        await callback.message.edit_text("Unknown style.")
        return

    try:
        original = callback.message.reply_to_message.text
        styled = func(original)
        msg = await callback.message.edit_text(
            f"`{styled}`\n\n👆 Click To Copy",
            reply_markup=callback.message.reply_markup
        )
        await asyncio.sleep(120)
        await callback.message.reply_to_message.delete()
        await msg.delete()
    except Exception as e:
        print("Error styling message:", e)
