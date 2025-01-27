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

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    );
""")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
