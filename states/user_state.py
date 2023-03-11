from aiogram.dispatcher.filters.state import StatesGroup, State


class register(StatesGroup):
    first_name = State()
    last_name = State()


class new_register(StatesGroup):
    new_first_name = State()
    new_last_name = State()
