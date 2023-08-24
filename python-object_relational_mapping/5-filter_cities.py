#!/usr/bin/python3
"""
script lists all cities from hbtn_0e_4_usa db
"""

import sys
import MySQLdb

# Arguments to be passed
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connects to server through port 3306 on localhost
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    # Creates cursor to execute queries
    cur = conn.cursor()

    # Creates query
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id"
    cur.execute(query, (state_name,))

    # Fetches & prints results
    results = cur.fetchall()
    city_names = [row[0] for row in results]
    print(', '.join(city_names))

    # Closes cursor & connection
    cur.close()
    conn.close()
