from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_game_start = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Начать игру', callback_data='game')
                                          ]
                                      ])
