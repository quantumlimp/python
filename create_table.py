import sqlite3

conn = sqlite3.connect("c/data/urls.db")

c = conn.cursor();

c.execute("CREATE TABLE
IF NOT EXISTS appointmentss (
 id integer PRIMARY KEY,
 date datetime NOT NULL,
 description text
)");

conn.commit()
conn.close()
