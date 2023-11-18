#!/usr/bin/python3

"""connects python script to a database"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # connect the db
    my_db = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], password=argv[2], db=argv[3])

    my_cursor = my_db.cursor()
    my_cursor.execute(
        """SELECT * FROM states WHERE name LIKE
        BINARY 'N%'ORDER BY states.id ASC
        """
        )

    states = my_cursor.fetchall()

    for state in states:
        print(state)

    my_cursor.close()
    my_db.close()
