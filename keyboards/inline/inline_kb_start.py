from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_start = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Регистрация', callback_data='reg')
                                     ]
                                 ])
