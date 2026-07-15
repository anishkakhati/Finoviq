import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Database Configuration
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Project Information
PROJECT_NAME = "Finoviq AI"
VERSION = "1.0.0"