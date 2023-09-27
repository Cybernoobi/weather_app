from db.base import connect_db, commit_and_close


def create_users_tables():
    conn, cursor = connect_db('../weather.db')

    sql = '''
        DROP TABLE IF EXISTS users;
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT
        );
    '''
    cursor.executescript(sql)
    commit_and_close(conn)


def create_weather_tables():
    conn, cursor = connect_db('../weather.db')
    sql = '''
        DROP TABLE IF EXISTS weather;
        CREATE TABLE IF NOT EXISTS weather(
            weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            tz INTEGER,
            sunrise DATETIME,
            sunset DATETIME,
            dt DATETIME,
            description TEXT,
            speed DECIMAL,
            temp DECIMAL,
            
            user_id INTEGER REFERENCES users(user_id) 
        );
    '''

    cursor.executescript(sql)
    commit_and_close(conn)


# create_weather_tables()
# create_users_tables()
