import sqlite3

db = sqlite3.connect('websiteblock.db')

cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS blocked (id INTEGER PRIMARY KEY AUTOINCREMENT, site_name TEXT, block_time TEXT, block_date TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS unblocked (id INTEGER PRIMARY KEY AUTOINCREMENT, site_name TEXT unblock_time TEXT, unblock_date TEXT)")
db.commit()