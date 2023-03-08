student ={}
def input_student():
    NoS = int(input("Number of student:"))
    for i in range(NoS):
        id = input("Student's ID: ")
        #input_student.append(id)
        name = str (input("Name of student: "))
        #input_student.append(name)
        DoB = input("Student's Date of Birth:")
        #input_student.append(DoB)
        student[id] = {"Name of the student": name,"Date of birth": DoB}
        print(f"Student {student[id]['Name of the student']} with ID {id} and date of birth is {student[id]['Date of birth']}")
input_student()
course={}
def input_course():
    NoC = int(input( "Number of Course:"))
    for i in range(NoC):
        CID = input("ID of the course:")
        #input_course.append(CID)
        NameC = input("Name of the course:")
        #input_course.append(NameC)
        course[CID]={"Name of the course": NameC}
        print(f" The course {course[CID]['Name of the course']} with ID {CID}")
input_course()
mark = {}
def input_mark():
   id = input("Enter the ID of the student:")
   CID = input("The ID of the course:")
   if id in student:
       if CID in course:
           mark=input("The mark of course:")
           #mark.append(mark)
           print(f"The mark of {course[CID]['Name of the course']} of {student[id]['Name of the student']} is:{mark}")
       if CID not in course:
           print("Try again!")
           return CID
   else:
       print("The info is wrong") 
       return
input_mark()


def main():
    input_student()
    input_course()
    mark()
    output()

main()



