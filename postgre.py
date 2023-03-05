import psycopg2

hostname = 'localhost'
database = 'pybot'
username = 'postgres'
pwd = '2103Finnick'
port_id = 5432

conn = None
cur = None
def database(user_userid:int, user_nickname:str, user_name:str, user_surname:str):
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
        cur = conn.cursor()

        create_script = """CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER, 
                    nickname TEXT,
                    name TEXT,
                    surname TEXT) """
        cur.execute(create_script)

        insert_script = "INSERT INTO users (user_id, nickname, name, surname) VALUES (%s, %s, %s, %s)"
        insert_value = (user_userid, user_nickname, user_name, user_surname)
        cur.execute(insert_script, insert_value)

        conn.commit()

    except Exception as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

