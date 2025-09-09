import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from flask import Flask
from threading import Thread

TOKEN = os.environ["TOKEN"]

# Web server biar selalu hidup
app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot Shopee jalan 🚀"

def run():
    app_flask.run(host="0.0.0.0", port=8080)

Thread(target=run).start()

# Bot Telegram
async def start(update, context):
    await update.message.reply_text("Halo! Bot Shopee siap jalan 🚀")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot running...")
app.run_polling()
