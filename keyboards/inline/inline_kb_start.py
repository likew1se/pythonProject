from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_start = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Инструкция', callback_data='instruction')
                                     ],
                                     [
                                         InlineKeyboardButton(text='Cvtest', callback_data='classify')
                                     ],

                                 ])
