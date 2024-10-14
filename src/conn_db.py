from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv(".env")
def load_data_to_postgres(data: pd.DataFrame, table_name: str):
    """
    Load data into a PostgreSQL database using SQLAlchemy.

    Parameters:
    -----------
    data : pd.DataFrame
        The data to be loaded into the database.
    
    table_name : str
        The name of the table where data should be inserted.

    Returns:
    --------
    None
    """
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASS')
    db_url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    try:
        # Create the SQLAlchemy engine
        engine = create_engine(db_url)

        # Load data into PostgreSQL
        data.to_sql(table_name, engine, if_exists='append', index=False)

        print(f"Data successfully loaded into the '{table_name}' table.")
        
    except Exception as e:
        print(f"Error loading data: {e}")

    finally:
        # Dispose of the engine connection after use
        engine.dispose()


def extract_data(table_name):
    """
    Extract data from a PostgreSQL database using SQLAlchemy.

    Parameters:
    -----------
    table_name : str
        The name of the table to extract data from.

    Returns:
    --------
    data : pd.DataFrame
        The data extracted from the database. 
    """
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASS')
    db_url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    try:
        # Create the SQLAlchemy engine
        engine = create_engine(db_url)

        # Load data into PostgreSQL
        data = pd.read_sql(f"SELECT * FROM {table_name} WHERE is_validate = True", engine)

        return data
        
    except Exception as e:
        print(f"Error loading data: {e}")

    finally:
        # Dispose of the engine connection after use
        engine.dispose()