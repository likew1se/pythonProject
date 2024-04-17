from aiogram.dispatcher.filters.state import StatesGroup, State


class register(StatesGroup):
    first_name = State()
    last_name = State()


class new_register(StatesGroup):
    new_first_name = State()
    new_last_name = State()


class dermatit(StatesGroup):
    dq1 = State()
    dq2 = State()
    dq3 = State()
    dq4 = State()
    dq5 = State()
    dq6 = State()
    dq7 = State()
    dq8 = State()


class akne(StatesGroup):
    aq1 = State()
    aq2 = State()
    aq3 = State()
    aq4 = State()
    aq5 = State()
    aq6 = State()