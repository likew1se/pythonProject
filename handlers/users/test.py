from aiogram.types import CallbackQuery
from keyboards.inline import ikb_yesno
from loader import dp


@dp.callback_query_handler(text='instruction')
async def instruction(call: CallbackQuery):
    await call.message.answer(f'Рекомендовано проводить самопроверку, которая заключается в осмотре кожи, не менее 1 раза в месяц. '
                              f'Самопроверка должна осуществляться в хорошо освещенной комнате, желательно, чтобы в комнате так же находилось зеркало в полный человечески рост. '
                              f'Можно использовать фонарик для лучшего освещения кожи.'
                              f'\nЧтобы осмотреть кожу спины, понадобится дополнительное зеркало. Можно прибегнуть к помощи друга или родственника.'
                              f'\nМожем предложить следующий порядок осмотра: волосистая часть головы - лицо - уши - шея - грудь - живот - подмышки - руки - ноги - область таза и гениталий - ягодицы - спина. Прилагаем фотографию доброкачественного образования:')
    await call.message.answer(f'Признаки доброкачественного образования:'
                              f'\n1. ровные края'
                              f'\n2. Симметричное '
                              f'\n3. Равномерный цвет'
                              f'\n4. Не изменяется в размерах в течение долгого времени')
    await call.message.answer(f'Если Вы обнаружили образование, не соответствующее данным критериям, предлагаем Вам пройти опрос.'
                              f'\nНужно отвечать только в формате да/нет', reply_markup=ikb_yesno)
