import psycopg2

from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def create_predictions_table():

    print("\nConnecting to PostgreSQL...\n")

    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = connection.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS predictions (

        id SERIAL PRIMARY KEY,

        company_id INTEGER NOT NULL,

        prediction_date DATE NOT NULL,

        predicted_open DOUBLE PRECISION,

        predicted_high DOUBLE PRECISION,

        predicted_low DOUBLE PRECISION,

        predicted_close DOUBLE PRECISION,

        model_name VARCHAR(100),

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    );

    """)

    connection.commit()

    cursor.close()

    connection.close()

    print("Predictions table created successfully!")


if __name__ == "__main__":

    create_predictions_table()