#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == '__main__':
    """ Arguments argv to connect to database
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    argv[4]: state name searched
    """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities JOIN states \
                ON cities.state_id = states.id ORDER BY cities.id")
    [print(", ".join([c[2] for c in cur.fetchall() if c[4] == sys.argv[4]]))]
