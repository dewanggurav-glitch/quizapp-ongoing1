import mysql.connector

print("Starting table creation...")

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="quiz_app"
)

cursor = connection.cursor()

# Admin table
cursor.execute("""
CREATE TABLE IF NOT EXISTS admins (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

# Categories table
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) UNIQUE NOT NULL
)
""")

# Questions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    question TEXT NOT NULL,
    option_a VARCHAR(255),
    option_b VARCHAR(255),
    option_c VARCHAR(255),
    option_d VARCHAR(255),
    correct_option ENUM('A','B','C','D'),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
)
""")

connection.commit()
print("✅ All tables created successfully")

cursor.close()
connection.close()
print("🔒 Connection closed")
