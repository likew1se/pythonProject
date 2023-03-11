from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu2 = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
[
                                        InlineKeyboardButton(text='Сообщение', callback_data='Сообщение')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Ссылка', url='https://github.com/likew1se')
                                    ]
                                ])