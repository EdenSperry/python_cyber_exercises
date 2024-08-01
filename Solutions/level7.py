import sqlite3

# Connect to an in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a table
cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')

# Insert a user safely
username = "john_doe"
password = "password123"
cursor.execute(
    'INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
conn.commit()

# Vulnerable function (SQL Injection possible)


def login_vulnerable(username, password):
    query = f"SELECT * FROM users WHERE username = '{
        username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()

# Secure function


def login_secure(username, password):
    query = 'SELECT * FROM users WHERE username = ? AND password = ?'
    cursor.execute(query, (username, password))
    return cursor.fetchone()


# Secure Query Execution: This function uses parameterized queries to safely inject user input into the SQL statement. The ? placeholders ensure that input is treated as data rather than executable code, thus preventing SQL injection.
# Test the secure login
result = login_secure("john_doe", "password123")
if result:
    print("Login successful!")
else:
    print("Login failed!")


# Test the vulnerable login
dangerous_input = "john_doe' OR '1'='1"
result = login_vulnerable(dangerous_input, "")
if result:
    print("Vulnerable login successful!")
else:
    print("Vulnerable login failed!")

# Vulnerable Query Construction: This function constructs an SQL query using string interpolation(f-strings in this case). The username and password are directly included in the query string.
# SQL Injection Vulnerability: If the username or password contains malicious SQL code, it could be executed, leading to SQL injection attacks. For example, if the username is set to "john_doe' OR '1'='1", the query becomes:
# - SELECT * FROM users WHERE username = 'john_doe' OR '1'='1' AND password = ''
# - This query will always return true because '1' ='1' is always true, potentially allowing unauthorized access.
