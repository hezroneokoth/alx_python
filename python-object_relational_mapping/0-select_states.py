#!/usr/bin/python3
""" This script lists all states from the database hbtn_0e_0_usa. """

import MySQLdb

# Arguments to be passed
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connects to MySQL server thru port 3306 on localhost
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

    # Executes the query
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetches & prints results
    results = cur.fetchall()
    for row in results:
        print(row)

    # Closes the cursor & connection
    cur.close()
    conn.close()
