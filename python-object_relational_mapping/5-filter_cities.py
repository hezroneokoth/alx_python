#!/usr/bin/python3
"""
cript lists all cities from hbtn_0e_4_usa db
"""

# import modules
import sys
import MySQLdb

# arguments to be passed
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

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

    # executes query
    query = "SELECT * FROM cities ORDER BY cities.id"
    cur.execute(query)

    # fetches & prints results
    results = cur.fetchall()
    for row in results:
        print(row)

    # closes cursor & connection
    cur.close()
    conn.close()