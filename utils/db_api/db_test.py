import asyncio

from data import config
from utils.db_api import quick_commands as commands
from utils.db_api.db_gino import db


async def db_test():
    # await db.set_bind(config.POSTGRES_URI)
    # await db.gino.drop_all()
    # await db.gino.create_all()

    # await commands.add_user(1, 'Egor', 'Net')
    # await commands.add_user(144, 'egor', '2323')
    # await commands.add_user(8, 'Egor', 'asdgg34')
    # await commands.add_user(22323567, 'aasdd', 'Имя')
    # await commands.add_user(909087, 'botssz', 'd4')

    users = await commands.select_all_users()
    print(users)

    count = await commands.count_users()
    print(count)

    user = await commands.select_user(1)
    print(user)

    await commands.update_user_name(1, 'name')

    user = await commands.select_user(1)
    print(user)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(db_test())
