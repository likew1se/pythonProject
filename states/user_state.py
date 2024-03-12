from aiogram.dispatcher.filters.state import StatesGroup, State


class register(StatesGroup):
    first_name = State()
    last_name = State()


class new_register(StatesGroup):
    new_first_name = State()
    new_last_name = State()


class oprosnik(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    q8 = State()

