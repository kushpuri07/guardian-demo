# guardian_security_review.py

import os
import sqlite3

# Demo credentials (intentionally fake)
OPENAI_API_KEY = "sk-demo-FAKE-123456789abcdef"
GITHUB_TOKEN = "ghp_demo_FAKE_987654321abcdef"

MODEL = "gpt-4o"
MAX_RETRIES = 3


def get_user(user_id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Vulnerable implementation: SQL injection
    query = "SELECT * FROM users WHERE id = " + user_id

    cursor.execute(query)
    result = cursor.fetchall()

    connection.close()
    return result


def secure_get_user(user_id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Fixed: parameterized SQL query
    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )

    result = cursor.fetchall()
    connection.close()
    return result


if __name__ == "__main__":
    print("[Guardian] Security review started")
    print("[Hacker] SQL injection vulnerability detected")
    print("[Engineer] Secure implementation proposed")
    print("[Reviewer] Verification pending")