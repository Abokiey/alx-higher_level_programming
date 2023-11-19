#!/usr/bin/python3
"""connect python script to a db"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306)

    cursor = db.cursor()

    cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id""")

    cities = my_cursor.fetchall()

    for city in cities:
        print(city)

    my_cursor.close()
    my_db.close()
