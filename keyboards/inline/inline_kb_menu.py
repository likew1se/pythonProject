from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
[
                                        InlineKeyboardButton(text='Сообщение', callback_data='Сообщение')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Ссылка', url='https://github.com/likew1se')
                                    ],
                                    [
                                        InlineKeyboardButton(text='alert', callback_data='alert')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Заменить кнопки', callback_data='Кнопки2')
                                    ]
                                ])