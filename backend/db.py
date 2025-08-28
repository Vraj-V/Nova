import sqlite3
sqlite3.enable_callback_tracebacks(True)
conn = sqlite3.connect("Jarvis//nova.db")

cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)


query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100),url VARCHAR(1000))"
cursor.execute(query)

# query ="INSERT INTO sys_command VALUES (null,'Epic Games Launcher','C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs')"
# cursor.execute(query)

query = "DELETE FROM web_command WHERE name='dude'"
cursor.execute(query)

# query ="INSERT INTO web_command VALUES (null,'whatsapp','https://web.whatsapp.com/')"
# cursor.execute(query)

# query ="INSERT INTO web_command VALUES (null,'react','https://tutedude.com/')"
# cursor.execute(query)
conn.commit()
conn.close()