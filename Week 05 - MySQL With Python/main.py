import StudentDBAccess

# menu based interface to the university database

# retrieve and display all students records that match the major input by the user
def do_retrieve_by_major():
    print("Enter the major")
    major = input()
    students = StudentDBAccess.retrieve_by_major(major)
    if len(students) == 0:
        print("no students were found")
    else:
       for student in students:
         print("ID {} Name {} {} Major {} Credits {} ".format(student.id, student.fname, student.lname,
                                                             student.major, student.credits))

# Display the number of students in a given major, entered by the user
def do_count_by_major():
    print("Enter the major")
    major = input()
    students = StudentDBAccess.retrieve_by_major(major)
    print("There are {} students in the {} program".format(len(students), major))

# get student information from the user and insert a new record to the Student table
# using that information
def do_insert():
    print("Enter the id")
    sid = input()
    print("Enter the first name")
    fname = input()
    print("Enter the last name")
    lname = input()
    print("Enter the major")
    major = input()
    print("Enter number of completed credits")
    cred = input()
    if StudentDBAccess.insert_student(sid, fname, lname, major, cred):
        print("student was inserted")
    else:
        print("student was not inserted")

# get a student id from the user and retrieve and display the student record for that id
def get_by_id():
    print("Enter a student id")
    sid = input()
    student = StudentDBAccess.retrieve_by_id(sid)
    if student is None:
        print("Student with id=" + sid + " was not found")
    else:
        print("ID {} Name {} {} Major {} Credits {} ".format(student.id, student.fname, student.lname,
                                                             student.major, student.credits))

# retrieve and display all students records that match the number of credits input by the user
def do_retrieve_by_credits():
    print("Enter the number of credits")
    numcredits = input()
    students = StudentDBAccess.retrieve_by_credits(numcredits)
    if len(students) == 0:
        print("no students were found")
    else:
       for student in students:
         print("ID {} Name {} {} Major {} Credits {} ".format(student.id, student.fname, student.lname,
                                                             student.major, student.credits))

def do_update_major():
    print("Enter the id")
    sid = input()
    print("Enter the new major")
    newmajor = input()
    if StudentDBAccess.update_major(sid, newmajor):
        print("student's major was updated")
    else:
        print("student's major was not updated")

# start here
print("Have some Student Database Fun!")
print("Enter:\n\tA to retrieve students by major,\
         \n\tB the number of students in a major,\
         \n\tC to retrieve a student by Id,\
         \n\tD to retrieve students with greater than a certain number of credits,\
         \n\tI to insert a student,\
         \n\tU to update the major of a student,\
         \n\tQ to quit")
cmd = str.upper(input())

while cmd != 'Q':
    if cmd == 'A':
        do_retrieve_by_major()
    if cmd == 'B':
        do_count_by_major()
    if cmd == 'C':
        get_by_id()
    if cmd == 'D':
        do_retrieve_by_credits()
    if cmd == 'I':
        do_insert()
    if cmd == 'U':
        do_update_major()

    print("\nEnter:\n\tA to retrieve students by major,\
            \n\tB the number of students in a major,\
            \n\tC to retrieve a student by Id,\
            \n\tD to retrieve students by number of credits,\
            \n\tI to insert a student,\
            \n\tU to update the major of a student,\
            \n\tQ to quit")
    cmd = str.upper(input())

print("Bye!")
