from telegram import Bot
import asyncio
from config import TELEGRAM_TOKEN as api_token
# from os import getenv

bot = Bot(token=api_token)
chat_id = "5804749969"

async def message_sender(text):
    message_info = await bot.send_message(text, chat_id=chat_id)
    # last_message_id = message_info.message_id
    await bot.delete_message(message_id=message_info.message_id, chat_id=chat_id)
    
# if __name__ == "__main__":
asyncio.run(message_sender())



