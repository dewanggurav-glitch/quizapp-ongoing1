import mysql.connector

print("Starting database creation...")

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root"   # change if your MySQL password is different
    )

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS quiz_app")
    print("✅ Database 'quiz_app' created or already exists")

    cursor.execute("SHOW DATABASES")
    print("📦 Available databases:")
    for db in cursor.fetchall():
        print(db[0])

    cursor.close()
    connection.close()
    print("🔒 Connection closed")

except mysql.connector.Error as err:
    print("❌ MySQL Error:")
    print(err)
