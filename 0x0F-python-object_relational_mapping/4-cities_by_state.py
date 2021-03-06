#!/usr/bin/python3
'''
This script lists all cities from database 'hbtn_0e_4_usa'
'''

from sys import argv
import MySQLdb

if __name__ == '__main__':

    # declaring arguments passed, with query.
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    query = """SELECT cities.id, cities.name, states.name
FROM states INNER JOIN cities ON states.id = cities.state_id
ORDER BY cities.id ASC"""

    # creating connection to the database.
    db_connection = MySQLdb.connect(host="localhost", port=3306, user=user,
                                    passwd=passwd, db=db, charset="utf8")

    # Making a cursor Object for query execution.
    cursor = db_connection.cursor()

    # Executing query.
    cursor.execute(query)
    query_rows = cursor.fetchall()

    # Printing DATABASE
    for row in query_rows:
        print(row)

    cursor.close()
    db_connection.close()
