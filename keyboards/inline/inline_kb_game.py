from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_game = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Меланома', callback_data='mel')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Актинический кератоз/карцинома/болезнь Боуэна',
                                                             callback_data='akiec')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Базально-клеточная карцинома', callback_data='bcc')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Доброкачественные поражения', callback_data='bkl')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Дерматофиброма', callback_data='df')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Меланоцитарные невусы', callback_data='nv')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Сосудистые поражения', callback_data='vasc')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Закончить игру', callback_data='endgame')
                                    ]
                                ])
