import psycopg2

from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def save_model_results(
    model_name,
    mae,
    rmse,
    r2,
    mape,
    training_time
):
    """
    Save model evaluation metrics into PostgreSQL.
    """

    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = connection.cursor()

    query = """
    INSERT INTO model_results
    (
        model_name,
        mae,
        rmse,
        r2,
        mape,
        training_time
    )

    VALUES
    (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    );
    """

    cursor.execute(
    query,
    (
        model_name,
        float(mae),
        float(rmse),
        float(r2),
        float(mape),
        float(training_time)
    )
    )

    connection.commit()

    cursor.close()
    connection.close()

    print(f"\n {model_name} results saved into PostgreSQL!")