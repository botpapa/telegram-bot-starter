"""
Launch this file to start the bot
"""
from aiogram import executor
from aiogram.types import ContentTypes

from settings.bot import dispatcher


@dispatcher.message_handler(content_types=ContentTypes.all())
async def text_handler(message):
    await message.reply("It's working!")


# Starting bot polling
executor.start_polling(dispatcher)
