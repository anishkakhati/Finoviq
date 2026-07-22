import psycopg2
from psycopg2 import errors

from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def save_prediction(
    company_id,
    prediction_date,
    predicted_open,
    predicted_high,
    predicted_low,
    predicted_close,
    confidence=0.95,
    model_version="v1.0"
):

    # ==========================================
    # CONNECT TO DATABASE
    # ==========================================

    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = connection.cursor()

    # ==========================================
    # INSERT QUERY
    # ==========================================

    query = """
    INSERT INTO predictions
    (
        company_id,
        prediction_date,
        predicted_open,
        predicted_high,
        predicted_low,
        predicted_close,
        confidence,
        model_version
    )
    VALUES
    (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    );
    """

    try:

        cursor.execute(
            query,
            (
                company_id,
                prediction_date,
                float(predicted_open),
                float(predicted_high),
                float(predicted_low),
                float(predicted_close),
                float(confidence),
                model_version
            )
        )

        connection.commit()

        print("\nPrediction saved successfully into PostgreSQL!")

    except errors.UniqueViolation:

        connection.rollback()

        print("\nPrediction for today already exists in PostgreSQL.")

    finally:

        cursor.close()
        connection.close()