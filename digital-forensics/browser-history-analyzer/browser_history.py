import os
import sqlite3
import shutil

# Ask for folder path (Default folder)
folder_path = input("Enter Chrome Default folder path: ")

# Build full History file path
history_path = os.path.join(folder_path, "History")

# Create a temporary copy (Chrome locks the real file)
temp_history = "history_copy.db"
shutil.copy2(history_path, temp_history)

# Connect to the copied database
conn = sqlite3.connect(temp_history)
cursor = conn.cursor()

cursor.execute("SELECT url, last_visit_time FROM urls LIMIT 10")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
