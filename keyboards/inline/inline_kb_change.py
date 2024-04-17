from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_change = InlineKeyboardMarkup(row_width=1,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Изменить имя', callback_data='change')
                                      ],
                                      [
                                          InlineKeyboardButton(text='Начать игру', callback_data='game')
                                      ],
                                      [
                                          InlineKeyboardButton(text='Таблица лидеров', callback_data='leader')
                                      ],
                                      [
                                          InlineKeyboardButton(text='Посмотреть свой счет', callback_data='check')
                                      ]
                                  ])
