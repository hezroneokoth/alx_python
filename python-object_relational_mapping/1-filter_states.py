#!/usr/bin/python3
""" script lists all states starting with 'N' from hbtn_0e_0_usa db."""

import sys
import MySQLdb

# arguments to be passed
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connects to MySQL server thru port 3306 on localhost
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

    # executes the query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

    # fetches & prints results
    results = cur.fetchall()
    for row in results:
        print(row)

    # closes cursor & connection
    cur.close()
    conn.close()
