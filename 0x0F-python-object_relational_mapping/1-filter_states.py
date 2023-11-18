#!/usr/bin/python3

"""filter states"""

import sys
import MySQLdb

if __name__ = "__main__":
    """connect to db"""
    db = MySQLdb.connect(host="localhost"user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3], port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE
                   		BINARY 'N%' ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
