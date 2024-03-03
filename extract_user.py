import sqlite3

# Connect to the database
db = sqlite3.connect("websiteblock.db")

# Create a cursor object
cursor = db.cursor()

# Execute the SELECT statement
cursor.execute("SELECT id, username, password FROM users")

# Fetch all the rows from the result
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    id, username, password = row
    print("ID:", id)
    print("Username:", username)
    print("Password:", password)
    print()

# Close the cursor and database connection
cursor.close()
db.close()
