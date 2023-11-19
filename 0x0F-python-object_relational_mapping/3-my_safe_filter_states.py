#!/usr/bin/python3
"""connects a python script to a db"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306
        )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states  WHERE name=%s ORDER BY id", (argv[4], ))

    states = my_cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
