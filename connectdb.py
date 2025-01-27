import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="your_dbname", 
    user="your_username", 
    password="your_password", 
    host="localhost", 
    port="5432"
)

# Create a cursor object
cursor = conn.cursor()

# Use the cursor to execute queries...
cursor.execute("SELECT version();")

# Fetch and display the result
result = cursor.fetchone()
print(result)

# Close the cursor and connection
cursor.close()
conn.close()
