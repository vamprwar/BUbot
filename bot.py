from keep_alive import keep_alive
import os
import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update, context):
    update.message.reply_text("Бот запущен! Всё работает.")

def main():
    keep_alive()
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    if not TOKEN:
        raise Exception("Переменная окружения TELEGRAM_TOKEN не установлена!")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
