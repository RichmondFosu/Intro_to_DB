import mysql.connector

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='yourpassword'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database created successfully")

            print("database 'alx_books_store created' successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()