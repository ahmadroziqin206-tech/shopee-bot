import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Ambil token dari environment variable
TOKEN = os.environ["TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot Shopee siap jalan 🚀")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Kamu ngetik: {text}")

def main():
    app = Application.builder().token(TOKEN).build()

    # command /start
    app.add_handler(CommandHandler("start", start))

    # echo semua pesan teks
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
