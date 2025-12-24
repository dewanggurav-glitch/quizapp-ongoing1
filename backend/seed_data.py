import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="quiz_app"
)

cursor = connection.cursor()

# Insert admin (temporary password)
cursor.execute("""
INSERT IGNORE INTO admins (username, password)
VALUES ('admin', 'admin123')
""")

# Insert categories
categories = ['science', 'history', 'gk', 'it', 'ca']
for cat in categories:
    cursor.execute(
        "INSERT IGNORE INTO categories (category_name) VALUES (%s)",
        (cat,)
    )

connection.commit()
print("✅ Admin & categories inserted")

cursor.close()
connection.close()
