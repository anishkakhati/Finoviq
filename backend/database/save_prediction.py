import psycopg2
from psycopg2 import errors

from backend.database.db import get_connection


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

    connection = get_connection()

    cursor = connection.cursor()

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
        %s,%s,%s,%s,%s,%s,%s,%s
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

        print(" Prediction saved successfully!")

    except errors.UniqueViolation:

        connection.rollback()

        print("Prediction already exists.")

    finally:

        cursor.close()

        connection.close()