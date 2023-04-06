import asyncio
import os
from sqlalchemy import func
from data import config
from utils.db_api.db_gino import db

from utils.db_api.schemas.test import File
PATH_TO_FILE = 'http://rodinka.lpt.digital/images/'


async def get_dirname(filename):
    # await db.set_bind(config.POSTGRES_URI)
    image = await File.query.where(File.filename == filename).gino.first()
    dir = image.dirname
    return dir


async def select_random_image():
    # await db.set_bind(config.POSTGRES_URI)
    image = await File.query.order_by(func.random()).gino.first()
    strimage = str(image).split()
    res = [int(i) for i in strimage[1] if i.isdigit()]
    image = ''.join(map(str, res))
    file = await File.query.where(File.file_id == int(image)).gino.first()
    filename = str(file.filename)
    return filename

# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_dirname(select_random_image()))
