
import psycopg2


try:
    conn = psycopg2.connect("dbname='base_covered' user='dbuser' host='localhost' password='bases'")
except:
    print "Oops unable to connect to database"

if conn:
    db = conn.cursor()

#Obtain student data
def get_student(pcp_id):
    try:
        db.execute("SELECT * from students where pcp_id=%(id)s",{ 'id': pcp_id} )
        rows = db.fetchall()
    except:
        print "Error: Unable to find student(s)"
        return None

    return rows

def add_student(pcp_id, name, school):
    try:
        db.execute("INSERT INTO students(pcp_id, name, school) VALUES ("+pcp_id +", "+ name + ", " + school+")")
        db.commit()
    except:
        print "Error: Unable to add student"
        return false
    return true;

def remove_student(student_name, pcp_id):
    try:
        found =db.execute("SELECT * FROM students WHERE pcp_id = "+ pcp_id + "AND students.name = " + student_name)
        if found:
           rows = db.fetchall()

        else:
            print "Data not found"
            return false;








