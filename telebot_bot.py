import telebot
import google.auth
from google.cloud import storage

# توكن بوت تيليغرام
TELEGRAM_BOT_TOKEN = "7511938455:AAE99I9njQWTe7NIe9vqEIgiWB9f_Z8KnR0"
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# مصادقة Google Cloud
credentials, project = google.auth.load_credentials_from_file("service-account.json")
storage_client = storage.Client(credentials=credentials, project=project)

# إرسال رسالة عند تلقي أي رسالة
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, f"مرحبًا! مشروعك في Google Cloud هو: {project}")

print("🤖 Bot is running...")
bot.polling()