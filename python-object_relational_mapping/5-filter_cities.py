#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa.
Safe from SQL injection using parameterized queries.
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

    # Execute query using parameterized query to get cities
    # for a specific state
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""
    cursor.execute(query, (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Display results - only city names separated by commas
    city_names = [city[1] for city in results]
    print(", ".join(city_names))

    # Close cursor and database connection
    cursor.close()
    db.close()
