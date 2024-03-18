from aiogram import types
from aiogram.dispatcher import FSMContext
from states import get_photo
from data.config import PHOTO_DIR


import cv2
import numpy as np
import tensorflow as tf
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions

from filters import IsPrivate
from keyboards.inline import ikb_start
from utils.misc import rate_limit
from loader import dp
from utils.db_api import quick_commands as commands

model = ResNet50(weights='imagenet')

@dp.message_handler(IsPrivate(), text='/test')
async def profile(message: types.Message, state: FSMContext):
    await message.answer('Пришлите фотографию')
    await get_photo.photo_file.set()


@dp.message_handler(state=get_photo.photo_file)
async def user_photo(message: types.Message, state: FSMContext):
    if message.photo[0]:
        answer = message.photo[0]
        image_file = await message.bot.get_file(answer.file_id)

    else:
        await message.answer('Нужна фотография')

#    if message.photo:
#        photo = message.photo[0]
#        bot_image = await message.bot.download_file(photo)
#
#        img = image.load_img(bot_image, target_size=(224, 224))
#        x = image.img_to_array(img)
#        x = np.expand_dims(x, axis=0)
#        x = preprocess_input(x)
#
#        preds = model.predict(x)
#        print('Классификация изображения:', decode_predictions(preds, top=3)[0])
#        await message.answer('Классификация изображения: ' + str(decode_predictions(preds, top=3)[0]))
#    else:
#        await message.answer('Пожалуйста, отправьте изображение для классификации')