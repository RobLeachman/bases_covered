
import psycopg2


try:
    conn = psycopg2.connect("dbname='base_covered' user='dbuser' host='localhost' password='bases'")
except:
    print "Oops unable to connect to database"


