#!/usr/bin/python3
"""
Script that displays all values in the states table
where name matches the argument.
Safe from MySQL injection attacks using parameterized queries.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute query using parameterized query (safe from SQL injection)
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Display results
    for state in results:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
