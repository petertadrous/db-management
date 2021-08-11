import mysql.connector

from DBConnect import DBConnect

from collections import namedtuple

# retrieves the student record where the student id matches the value in the parameter
# returns a namedtuple Student
def retrieve_by_id(sid):
    try:
      dbconnect = DBConnect("university")
      conn = dbconnect.connect()
      cursor = conn.cursor(dictionary=True)
      query = "SELECT stuId,  lastName, firstName, major, credits from student where stuId = %s"
      cursor.execute(query, (sid,))  # you must put the comma after id
      print(cursor.statement)
      row = cursor.fetchone()
      if row is None:
        student = None
      else:
        student = build_student(row)

      cursor.close()
      conn.close()
      return student
    except mysql.connector.Error as e:
      print(e)
      return None


# retrieves student records where the major matches the value in the parameter
# returns a list of Student namedtuples
def retrieve_by_major(major):
    try:
      dbconnect = DBConnect("university")
      conn = dbconnect.connect()
      cursor = conn.cursor(dictionary=True)
      query = "SELECT stuId,  lastName, firstName, major, credits from student where major = %s"
      cursor.execute(query, (major,))  # you must put the comma after major

      print(cursor.statement)
      # this will return multiple rows
      students = []
      for row in cursor:
        student = build_student(row)
        students.append(student)
      cursor.close()
      conn.close()
      return students
    except mysql.connector.Error as e:
      print(e)
      return []


# retrieves student records where the num of credits is greater than the value in the parameter
# returns a list of Student namedtuples
def retrieve_by_credits(numcredits):
    try:
      dbconnect = DBConnect("university")
      conn = dbconnect.connect()
      cursor = conn.cursor(dictionary=True)
      query = "SELECT stuId,  lastName, firstName, major, credits from student where credits > %s"
      cursor.execute(query, (numcredits,))

      print(cursor.statement)
      # this will return multiple rows
      students = []
      for row in cursor:
        student = build_student(row)
        students.append(student)
      cursor.close()
      conn.close()
      return students
    except mysql.connector.Error as e:
      print(e)
      return []


# updates the major of one record into the Student table
# returns boolean - true if insert succeeded, false otherwise
def update_major(sid, newmajor):
    try:
      dbconnect = DBConnect("university")
      conn = dbconnect.connect()
      query = "UPDATE student SET major = %s WHERE stuID = %s"
      cursor = conn.cursor()
      cursor.execute(query, (newmajor,sid))
      conn.commit()
      print(cursor.statement)
      cursor.close()
      conn.close()
      return True
    except mysql.connector.Error as e:
        print(e)
        return False


# inserts one record into the Student table
# returns boolean - true if insert succeeded, false otherwise
def insert_student(sid, fname, lname, major, creds):
    try:
      dbconnect = DBConnect("university")
      conn = dbconnect.connect()
      query = "INSERT INTO student (stuID, firstName, lastName, major, credits) VALUES(%s,%s,%s,%s,%s)"
      cursor = conn.cursor()
      cursor.execute(query, (sid, fname, lname, major, creds))
      conn.commit()
      print(cursor.statement)
      cursor.close()
      conn.close()
      return True
    except mysql.connector.Error as e:
        print(e)
        return False

# create a Student namedtuple from a row in the cursor
def build_student(row):
    Student = namedtuple('Student', ['id', 'fname', 'lname', 'major', 'credits'])
    curr_student = Student(row['stuId'], row['lastName'], row['firstName'],
                          row['major'], row['credits'])
    return curr_student
