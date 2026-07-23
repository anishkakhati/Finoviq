import psycopg2

from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def get_connection():

    return psycopg2.connect(

        host=DB_HOST,

        port=DB_PORT,

        database=DB_NAME,

        user=DB_USER,

        password=DB_PASSWORD

    )


def connect_database():

    try:

        connection = get_connection()

        print(" Successfully Connected to PostgreSQL!")

        connection.close()

    except Exception as error:

        print(" Database Connection Failed")

        print(error)


def get_company_id(symbol):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(

        "SELECT id FROM companies WHERE symbol=%s;",

        (symbol,)

    )

    result = cursor.fetchone()

    cursor.close()

    connection.close()

    if result:

        return result[0]

    return None


if __name__ == "__main__":

    connect_database()