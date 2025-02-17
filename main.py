from flask import Flask, request
import telebot
import os

TOKEN = "7511938455:AAE99I9njQWTe7NIe9vqEIgiWB9f_Z8KnR0"  # ضع توكن البوت هنا
bot = telebot.TeleBot(TOKEN)

SOURCE_CHANNEL = -1002467389309  # ضع ID القناة المصدر (يجب أن يكون بصيغة عددية)
TARGET_CHANNEL = -1002375010266 # ضع ID القناة الهدف
WORD_TO_REMOVE = "@Cointelegraph"  # الكلمة المطلوب إزالتها

app = Flask(__name__)

@bot.message_handler(content_types=['text'])
def forward_message(message):
    """يقوم بإعادة توجيه الرسائل بعد تعديلها"""
    if message.chat.id == SOURCE_CHANNEL:
        modified_text = message.text.replace(WORD_TO_REMOVE, "")
        bot.send_message(TARGET_CHANNEL, modified_text)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    """يستقبل التحديثات من Webhook"""
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://YOUR_VERCEL_PROJECT.vercel.app/{TOKEN}")  # ضع رابط Vercel هنا
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
