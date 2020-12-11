from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_book(book):
    query = "INSERT INTO book(book_id,title,publish_date, description) " \
            "VALUES(%s,%s,%s,%s)"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, book)

        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()

def main():
    books = [(3,'Learn SQL Server', CURTIME(),'this is a book on SQL Server'),
             (4,'Learn DB2', CURTIME(),'this is a book on DB2'),
             (5,'Learn Aurora', CURTIME(),'this is a book on amazon Aurora')]
    insert_book(book)

if __name__ == '__main__':
    main()
