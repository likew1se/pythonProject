from aiogram.types import ContentType, Message

from loader import dp
from utils.db_api.test import select_random_image


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message.handler(text='/photo')
async def send_photo(message: Message):
    photos = await select_random_image()
    await dp.bot.send_photo(chat_id=message.from_user.id, photo='')