import sqlite3
def getConnection():
    return sqlite3.connect("data.db")

def createTables():
    conn = getConnection()
    try:
        conn.execute('''
        create table enquiry(id integer primary key,
                            student_name varchar(50) not null,
                            phone varchar(10) not null,
                            course_name varchar(50) not null)
        ''')
    except Exception as e:
        print(e)
    finally:
        conn.close()

def addEnquiry(student_name, phone, course_name):
    conn = getConnection()
    try:
        conn.execute('''
        insert into enquiry(student_name, phone, course_name) 
                    values(?, ?, ?)
        ''',(student_name,phone,course_name))
        conn.commit()
        return "success"
    except Exception as e:
        print(e)
        return "failure"
    finally:
        conn.close()
    
def getEnquiries():
    conn = getConnection()
    try:
        enquiries = conn.execute('''
        select * from enquiry
        ''').fetchall()
        return enquiries
    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()
    

if __name__ == "__main__":
    createTables()
    print(addEnquiry("chandan","9988998899","Python"))
    addEnquiry("vittal","9977998899","Python")
    addEnquiry("Adesh","9977665544","Java")
    print(getEnquiries())
