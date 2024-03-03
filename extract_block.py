import sqlite3

db = sqlite3.connect("websiteblock.db")

cursor = db.cursor()

cursor.execute("SELECT site_name, block_time, block_date FROM blocked")

rows = cursor.fetchall()

for row in rows:
    site_name, block_time, block_date = row
    print("Site name:", site_name)
    print("Block time:", block_time)
    print("Block date:", block_date)
    print()

cursor.close()
db.close()
