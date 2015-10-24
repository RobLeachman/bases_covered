
import psycopg2


try:
    conn = psycopg2.connect("dbname='base_cover' user='postgres'")
    db = conn.cursor()
except:
    print("Oops unable to connect to database")


#Obtain student data
def get_student(pcp_id):
    try:
        db.execute("SELECT * from students where pcp_id=%(id)s",{ 'id': pcp_id} )
        rows = db.fetchall()
    except:
        print("Error: Unable to find student(s)")
        return None

    return rows

def add_student(pcp_id, name, school):
    try:
        db.execute("INSERT INTO students(pcp_id, name, school) VALUES ("+pcp_id +", "+ name + ", " + school+")")
        db.commit()
        return True
    except:
        print("Error: Unable to add student")
        return False


def remove_student(student_name, pcp_id):
    try:
        found =db.execute("SELECT * FROM students WHERE pcp_id = "+ pcp_id + "AND students.name = " + student_name)
        if found:
            rows = db.fetchall()
            for row in rows:
                if student_name == row['name']:
                    selected_row = row
            if selected_row:
                db.execute("DELETE student WHERE id = "+selected_row['id'])
                return True
            else:
                return False
        else:
            print ("Data not found")
            return False;
    except:
        print("Error")

def add_pcp(name):
    try:
        db.execute("INSERT INTO pcp(name) VALUES ('"+ name+"')")
        conn.commit()
        return True
    except:
        print("Error: Unable add User")
        return False


def remove_pcp(pcp_id):
    try:
        db.execute("DELETE FROM pcp WHERE id = '"+pcp_id+"'")
        conn.commit()
    except:
        print("Error")


def get_pcp(pcp_id):
    try:
       #db.execute("SELECT * from pcp where pcp_id=%(id)s",{ 'id': pcp_id} )
        db.execute("SELECT * from pcp where id = " + pcp_id)
        rows = db.fetchall()
        return rows
    except:
        print("Error: Unable to find Primary Care Provider")
        return None


def get_itp(pcp_id):
    try:
        db.execute("SELECT * from itp where pcp_id=%(id)s",{ 'id': pcp_id} )
        rows = db.fetchall()
    except:
        print("Error: Unable to find Interested Third Party")
        return None

    return rows

def add_itp(pcp_id, name):
    try:
        db.execute("INSERT INTO itp(pcp_id, name) VALUES ("+pcp_id +", "+ name+")")
        db.commit()
        return True
    except:
        print("Error: Unable to add student")
        return False


def remove_itp(itp_name, pcp_id):
    try:
        found =db.execute("SELECT * FROM students WHERE pcp_id = "+ pcp_id + "AND itp.name = " + itp_name)
        if found:
            rows = db.fetchall()
            for row in rows:
                if student_name == row['name']:
                    selected_row = row
            if selected_row:
                db.execute("DELETE student WHERE id = "+selected_row['id'])
                return True
            else:
                return False
        else:
            print ("Data not found")
            return False;
    except:
        print("Error")

def get_school(s_id):
    try:
        db.execute("SELECT * from schools where id=%(id)s",{ 'id': s_id} )
        rows = db.fetchall()
    except:
        print("Error: Unable to find School")
        return None

    return rows

def add_school( name):
    try:
        db.execute("INSERT INTO schools(name) VALUES ( '"+ name+"')")
        conn.commit()
        return True
    except:
        print("Error: Unable to add student")
        return False


def remove_school(s_id):
    try:
        db.execute("DELETE FROM pcp WHERE id = "+s_id)
        conn.commit()
    except:
        print("Error")

def get_events(s_id):
    try:
        db.execute("SELECT * from events where school_id=%(id)s",{ 'id': s_id} )
        rows = db.fetchall()
    except:
        print("Error: Unable to find School")
        return None

    return rows

def add_event(name,date,s_id):
    try:
        db.execute("INSERT INTO events(date, name, school_id) VALUES ('"+ date +"','"+name +"','"+s_id+"')")
        conn.commit()
        return True
    except:
        print("Error: Unable to add event")
        return False


def remove_event(s_id):
    try:
        db.execute("DELETE FROM events WHERE id = "+s_id)
        conn.commit()
    except:
        print("Error")


def add_assigned(name, date):
    try:
       db.execute("INSERT INTO assigned(assigned_name, date_assigned) VALUES ('" + name + "','" + date + "')")
       conn.commit()
       return True
    except:
       print("Error: Unable to assign care provider")
       return False

