from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Регистрация')
        ],
        [
            KeyboardButton(text='Любой текст')
        ],
        [
            KeyboardButton(text='Инлайн меню')
        ]
    ],
    resize_keyboard=True
)
