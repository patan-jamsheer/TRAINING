dict={
    42:{"name":"jamsheer","section":"csm-A"},
    41:{"name":"HITESH","section":"AI-ML"}
    }

def add():
    print("*"*50)  
    print("Enter the deatils of the student\n") 
    name=input("enter name of the student\n")
    section=input("enter the section\n")
    roll_no=int(input("enter the roll no\n"))
    with open("sample.txt","r") as f:
        data=f.read()
    unique="roll_no"+str(roll_no)
    if unique in data:
        print("Student already existed\n")
        print("*"*50)
        return
    else: 
        
        student={unique:{"name":name,"section":section}}
        with open("sample.txt","a") as f:
            f.write(str(student)+"\n")
        print("student successfully added\n")
        print("*"*50)


def view():
    with open("sample.txt","r") as f:
        data=f.read()
    if len(data)==0:
        print("No students were thier\n")
        print("*"*50)
    else:
        print("Students Data\n")
        print(data)
        print("*"*50)
def search():
    
    
    roll_no=int(input("enter the roll no for searching the student "))
    unique="roll_no"+str(roll_no)
    with open("sample.txt","r") as f:
            lines=f.readlines()
            for line in lines:
                if unique in line:
                    print("student found\n")
                    print(line)
                    return (1,roll_no)
    
    print("student not found\n")
    return (0,roll_no)
def delete():
    roll_no=int(input("enter the roll no for searching the student "))
    unique="roll_no"+str(roll_no)
    k=0
    with open("sample.txt","r") as f:
        lines=f.readlines()
        applines=""
        for line in lines:
            if unique in line:
                k=1
                continue
            else:
                applines+=line
        with open("sample.txt","w") as f1:
            f1.write(applines)
        if k==1:
            print("student successfully deleted\n")
        else:
            print("student not found\n")
    

def update():

    val,roll_no=search()
    if val==0:
        print("student not found\n")
    else:
        name=input("enter name of the student\n")
        section=input("enter the section\n") 
        unique="roll_no"+str(roll_no)
        k=0
        with open("sample.txt","r") as f:
            lines=f.readlines()
            applines=""
            for line in lines:
                if unique in line:
                    student={unique:{"name":name,"section":section}}
                    applines+=str(student)+"\n"
                else:
                    applines+=line
            with open("sample.txt","w") as f1:
                f1.write(applines)
            
            print("student successfully updated\n")
            
        

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
            
            

































