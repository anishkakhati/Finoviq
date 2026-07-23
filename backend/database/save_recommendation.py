import psycopg2
from psycopg2 import errors

from datetime import date

from backend.database.db import get_connection


def save_recommendation(

    company_id,

    recommendation,

    entry_price,

    exit_price,

    stop_loss,

    take_profit,

    expected_profit,

    expected_loss,

    roi,

    confidence,

):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO recommendations
    (
        company_id,
        recommendation_date,
        recommendation,
        entry_price,
        exit_price,
        stop_loss,
        take_profit,
        expected_profit,
        expected_loss,
        roi,
        confidence
    )
    VALUES
    (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
    );
    """

    try:

        cursor.execute(

            query,

            (

                company_id,

                date.today(),

                recommendation,

                float(entry_price),

                float(exit_price),

                float(stop_loss),

                float(take_profit),

                float(expected_profit),

                float(expected_loss),

                float(roi),

                float(confidence)

            )

        )

        connection.commit()

        print(" Recommendation saved successfully!")

    except errors.UniqueViolation:

        connection.rollback()

        print("Recommendation already exists.")

    finally:

        cursor.close()

        connection.close()