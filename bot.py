from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

TOKEN = "8647126204:AAEg80wQoRjR04HQpNlYyzblbaHbUT50neg"
VIP_LINK = "https://t.me/+c6cK0y1bYHc2M2Qy"

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = update.chat_join_request

    text = """Siz Just Forex kanalga zayavka yubordingiz.

🎁 Bonus sifatida VIP kanalimizga taklif 👇"""

    keyboard = [
        [InlineKeyboardButton("🚀 VIP KANAL", url=VIP_LINK)]
    ]

    await context.bot.send_message(
        chat_id=req.from_user.id,
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(join))

print("Bot ishladi...")

app.run_polling()
