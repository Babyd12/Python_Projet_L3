import sqlite3

conn = sqlite3.connect('work.db')
cur = conn.cursor()

# Creation de table
req = 'create table IF NOT EXISTS user(id integer primary key autoincrement, nom text, email text, password text, zone_message text, etat integer)'
#req = 'Drop table if exists user'
cur.execute(req)
# je demarre lexecution de la requette
conn.commit()
conn.close() # jarretre lexecutin de la requette




