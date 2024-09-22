from telegram import Bot
import asyncio
from os import getenv

api_token = "{}".format(getenv("membottg"))
bot = Bot(token=api_token)

chat_id = "5804749969"

text = "Вставай, заебал"
async def message_sender():
    message_info = await bot.send_message(text=text, chat_id=chat_id)
    print(message_info.chat.username)
    await bot.delete_message(message_id=message_info.message_id, chat_id=chat_id)
    
# if __name__ == "__main__":
asyncio.run(message_sender())



