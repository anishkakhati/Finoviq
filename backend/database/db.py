import psycopg2

from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def connect_database():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        print("✅ Successfully Connected to PostgreSQL!")

        connection.close()

    except Exception as error:
        print("❌ Database Connection Failed")
        print(error)


if __name__ == "__main__":
    connect_database()