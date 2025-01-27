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

# Insert data
cursor.execute("""
    INSERT INTO users (name, email) 
    VALUES (%s, %s);
""", ("Alice", "alice@example.com"))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
