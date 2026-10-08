dict={
    42:{"name":"jamsheer","section":"csm-A"},
    41:{"name":"HITESH","section":"AI-ML"}
    }
import mysql.connector

connection=mysql.connector.connect(
    user="root",
    database="student_management",
    host="localhost",
    password="Jamsheer@2006"
)
cursor=connection.cursor()
def add():
    print("*"*50)  
    print("Enter the deatils of the student\n") 
    name=input("enter name of the student\n")
    section=input("enter the section\n")
    roll_no=int(input("enter the roll no\n"))

    query="""select name,roll_no,section from students where roll_no=%s"""
    cursor.execute(query,(roll_no,))
    data=cursor.fetchone()
    if data:
        print("Student already existed\n")
        print("*"*50)
        return
    else:
        dict[roll_no]={"name":name,"section":section}
        f=open("sample.txt","a")
        f.write(str(dict[roll_no]))
        print("student successfully added\n")
        print("*"*50)


def view():
    if len(dict)==0:
        print("No students were thier\n")
        print("*"*50)
    else:
        print("Students Data\n")
        for key,value in dict.items():

            print(f"ROll_ NO={key}--NAME:{value['name']}--SECTION:{value['section']}")
            print("*"*50)
def search():
    
    roll_no=int(input("enter the roll no for searching the student "))
    if roll_no in dict.keys():
        print("student found\n")
        key=roll_no
        value=dict[roll_no]
        print(f"ROll_ NO={key}--NAME:{value['name']}--SECTION:{value['section']}")
    else:
        print("student not found\n")
def delete():
    roll_no=int(input("enter the roll no for searching the student "))
    if roll_no in dict.keys():
        del dict[roll_no]
        print("student deleted successfully\n")
    else:
        print("student not found\n")
    
def update():
    roll_no=int(input("enter the roll no for searching the student "))
    if roll_no in dict.keys():
        name=input("enter name of the student\n")
        section=input("enter the section\n")  
        dict[roll_no]['name']=name
        dict[roll_no]['section']=section 
        print("student updated successfully\n")
    else:
        print("student not found\n")


while True:
    print("*"*50)
    print("STudent Management system\n")
    print("1.ADD STUDENT\n")
    print("2.VIEW STUDENT\n")
    print("3.UPDATE STUDNET\n")
    print("4.DELETE STUDENT\n")
    print("5.SEARCH STUDENT\n")
    print("6.EXIT\n")
    print("*"*50)
    choice=int(input("enter the choice\n"))
    print("*"*50)
    match choice:
        case 1:
            add()
        case 2:
            view()
        case 3:
            update()
        case 4:
            delete()
        case 5:
            search()
        case 6:
            break
            
            

