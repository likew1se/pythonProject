from sqlalchemy import Column, BigInteger, String, sql

from utils.db_api.db_gino import BaseModel


class File(BaseModel):
    __tablename__ = 'images'
    file_id = Column(BigInteger, primary_key=True)
    filename = Column(String(200))
    dirname = Column(String(200))

    query: sql.select
