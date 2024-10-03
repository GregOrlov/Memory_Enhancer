from telegram import Bot
import asyncio
import os
from config import TELEGRAM_TOKEN as api_token
# from os import getenv

bot = Bot(token=api_token)
chat_id = "5804749969"

async def send_message(text, chat_id=chat_id): #sending message. SUDDENLY!
    message_info = await bot.send_message(chat_id=chat_id, text=text)
    last_message_id = message_info.message_id
    return last_message_id

async def delete_message(message_id, chat_id=chat_id):
    await bot.delete_message(chat_id=chat_id, message_id=message_id)

#working with last_message_id
def load_last_message():
    if os.path.exists("last_message.txt"):
        with open("last_message.txt", "r") as f:
            return int(f.read().strip())
    return None
def save_last_message(message_id):
    with open("last_message.txt", "w") as f:
        f.write(str(message_id))



    
# if __name__ == "__main__":
# asyncio.run(message_sender())



