from telethon import TelegramClient, events
import asyncio
import telebot_bot
import keep_alive
from keep_alive import keep_alive

keep_alive()

# Replace these with your values from https://my.telegram.org/apps
API_ID = '25140031'
API_HASH = 'a9308e99598c9eee9889a1badf2ddd2f'
PHONE_NUMBER = '+971569803058'

# Channel usernames (with or without @)
SOURCE_CHANNEL = '@cointelegraph'
TARGET_CHANNEL = '@crypto_N4'

# Initialize the client
client = TelegramClient('session_name', API_ID, API_HASH)

# Specify the word to remove from messages
WORD_TO_REMOVE = "@Cointelegraph"  # Change this to the word you want to filter out

async def send_code():
    try:
        print("Sending code...")
        await client.send_code_request(PHONE_NUMBER)
        code = input('Enter the code you received: ')
        await client.sign_in(PHONE_NUMBER, code)
    except Exception as e:
        print(f"Error during login: {e}")

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def send_message(event):
    try:
        # Modify the message by removing the specified word
        modified_message = event.message.text.replace(WORD_TO_REMOVE, "")
        await client.send_message(TARGET_CHANNEL, modified_message)
        print(f"Sent message: {modified_message[:50]}...")
    except Exception as e:
        print(f"Error sending message: {e}")

async def main():
    # Start the client
    await client.start()

    # If not logged in, send code
    if not await client.is_user_authorized():
        await send_code()

    print("Bot is running...")

    # Keep the bot running
    await client.run_until_disconnected()

# Run the bot
client.loop.run_until_complete(main())

from aiohttp import web

async def handle(request):
    return web.Response(text="Bot is running!")

app = web.Application()
app.router.add_get("/", handle)

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(bot.polling())  # تشغيل البوت
    web.run_app(app, port=10000)  # تشغيل سيرفر ويب

web.run_app()

import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running!"

if __name__ == "__main__":
    # الحصول على رقم المنفذ من متغير البيئة، وإذا لم يكن موجودًا نستخدم 5000
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
