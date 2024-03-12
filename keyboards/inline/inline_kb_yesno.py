from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_yesno = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Пройти опрос', callback_data='opros')
                                          ]
                                      ])
