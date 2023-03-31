from asyncpg import UniqueViolationError
import asyncio
from data import config

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(user_id: int, first_name: str, last_name: str, username: str, status: str, score: float):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username, status=status,
                    score=score)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):
    # await db.set_bind(config.POSTGRES_URI)
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def update_name(user_id, first_name, last_name):
    user = await select_user(user_id)
    await user.update(first_name=first_name, last_name=last_name).apply()


async def update_score(user_id):
    # await db.set_bind(config.POSTGRES_URI)
    user = await select_user(user_id)
    new_score = user.score + 1
    await user.update(score=new_score).apply()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(update_score(select_user(218824758)))