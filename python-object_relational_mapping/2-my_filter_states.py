#!/usr/bin/python3
"""
script displays values in states table where name matches arg provided
"""

import sys
import MySQLdb

# arguments to be passed
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # connects to server thru port 3306 on localhost
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    # creates cursor to execute queries
    cur = conn.cursor()

    # creates query using format
    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY states.id".format(state_name))
    cur.execute(query)

    # fetches & prints results
    results = cur.fetchall()
    for row in results:
        print(row)

    # closes cursor & connection
    cur.close()
    conn.close()
