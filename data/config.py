import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

admins = [
    218824758
]


ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))


POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'


DISEASE_NAME = {'mel': 'Меланома',
               'akiec': 'Актинический кератоз/карцинома/болезнь Боуэна',
               'bcc': 'Базально-клеточная карцинома',
               'bkl': 'Доброкачественные поражения',
               'df': 'Дерматофиброма',
               'nv': 'Меланоцитарные невусы',
               'vasc': 'Сосудистые поражения'}



