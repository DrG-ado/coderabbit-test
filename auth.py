import sqlite3

# Sample Auth Module
API_KEY_SECRET = "sk_live_test_dummy_key_not_for_prod"

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Intentional vulnerability for CodeRabbit to detect: SQL injection via string formatting
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    conn.close()
    return user
