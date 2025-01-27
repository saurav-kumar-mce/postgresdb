import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname="your_dbname", 
    user="your_username", 
    password="your_password", 
    host="localhost", 
    port="5432"
)
cursor = conn.cursor()

# Select data from users table
cursor.execute("SELECT * FROM users;")

# Fetch and display all rows
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
