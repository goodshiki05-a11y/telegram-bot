from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

TOKEN = "8647126204:AAGbOEu1kIlVDQRM-14SYWLC8hDyBrXWyeI"

VIP_LINK_1 = "https://t.me/+op27YdlLqpo5ZmEy"
VIP_LINK_2 = "https://t.me/+3TAQgBgnShhiZTU6"

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = update.chat_join_request

    text = """𝗦𝗶𝘇𝗻𝗶𝗻𝗴 ᴊᴜꜱᴛ ꜰᴏʀᴇx 𝗞𝗔𝗡𝗔𝗟𝗜𝗚𝗔 𝗾𝗼'𝘀𝗵𝗶𝗹𝗶𝘀𝗵 𝘀𝗼'𝗿𝗼𝘃𝗶𝗻𝗴𝗶𝘇 𝗺𝘂𝘃𝗮𝗳𝗳𝗮𝗾𝗶𝘆𝗮𝘁𝗹𝗶 𝘁𝗮𝘀𝗱𝗶𝗾𝗹𝗮𝗻𝗱𝗶 ✅

🎁 𝗦𝗶𝘇𝗴𝗮 𝗯𝗼𝗻𝘂𝘀 𝘀𝗶𝗳𝗮𝘁𝗶𝗱𝗮 𝗯𝗶𝘇𝗻𝗶𝗻𝗴 𝗩𝗜𝗣 𝘃𝗮 𝗥𝗔𝗭𝗚𝗢𝗡 𝗞𝗔𝗡𝗔𝗟𝗟𝗔𝗥𝗜𝗠𝗜𝗭 𝗾𝗼‘𝘀𝗵𝗶𝗯 𝗯𝗲𝗿𝗶𝗹𝗱𝗶❗️"""

    keyboard = [
        [InlineKeyboardButton("VIP KANAL 1", url=VIP_LINK_1)],
        [InlineKeyboardButton("VIP KANAL 2", url=VIP_LINK_2)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=req.user_chat_id,
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(join))

print("Bot ishladi o'chirib qo'yma...")

app.run_polling()

