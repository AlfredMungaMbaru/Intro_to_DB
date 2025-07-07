#!/usr/bin/env python3

import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to the MySQL server (adjust user, password, and host as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )

        cursor = connection.cursor()

        # Try to create database (if it exists, catch error)
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")

    except mysql.connector.Error as err:
        print("Error: Could not connect to the MySQL server.")
        print(f"MySQL Error: {err}")

    finally:
        # Ensure resources are cleaned up
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
