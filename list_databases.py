import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "Trusted_Connection=yes;"
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # List all databases
    cursor.execute("SELECT name FROM sys.databases")
    databases = cursor.fetchall()

    print("Available Databases:")
    for db in databases:
        print(db[0])

    # Close the connection
    conn.close()

except Exception as e:
    print(f"Error: {e}")
