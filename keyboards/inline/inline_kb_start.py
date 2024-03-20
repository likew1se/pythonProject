from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_start = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Тренажер', callback_data='train')
                                     ],
[
                                         InlineKeyboardButton(text='Ситуационные задаич',
                                                              callback_data='stt')
                                     ],
                                     [
                                         InlineKeyboardButton(text='Клинические рекомендации', callback_data='cr')
                                     ],
                                     [
                                         InlineKeyboardButton(text='Статистика', callback_data='stats')
                                     ],
                                     [
                                         InlineKeyboardButton(text='Условия подписки', callback_data='sub')
                                     ],
                                 ])
