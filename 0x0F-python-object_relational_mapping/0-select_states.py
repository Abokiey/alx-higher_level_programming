#!/usr/bin/python3

"""import modules"""

import MySQLdb
import sys

if __name__ == "__main__":
    """connect to the server"""
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    """prepare cursor object"""
    cursor = db.cursor()

    """execute the cursor"""
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
