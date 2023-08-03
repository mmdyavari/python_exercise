import os , platform

all_students = [
    {"name":"korush", "math":0, "computer":0},
    {"name":"miad", "math":0, "computer":0},
    {"name":"mohammad", "math":0, "computer":0},
    {"name":"reza", "math":0, "computer":0},
]

def clear_terminal ():
    sys_name = platform.system()
    if sys_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clear_terminal()


def set_mark (name = ''):
    if not name :
        name = input("Ente student's name : ")

    for i in all_students:
        if i['name'] == name:
            for stu in i:
                if stu != "name":
                    i.update({stu : float(input(f"Enter {stu}'s mark : "))})
            
            nums = list(i.values())
            nums.remove(name)
            i.update({"average" : round(sum(nums)/2 , 2)})
            print(i)


def add_student ():
    name = input("Enter user name : ")
    for i in all_students:
        if i["name"] == name:
            print(f"sorry {name} is our student :(")
            break
    else:
        lessons = list(all_students[0].keys())
        student = {"name":name}
        for i in lessons:
            if i != 'name':
                student.update({i : 0})
        all_students.append(student)
        print(f"{name} add :)")

    
def student_info (name = ''):
    if not name :
        name = input("Ente name for student : ")
        
    for i in all_students:
        if i['name'] == name:
            for key in i:
                print(f"{key} : {i[key]}")
    else:
        print("we don't have this student :(")

while True:
    print("""
    set mark for student (a)
    add a new student (b)
    show information of a student (c)
    close app (end)
    """)
    plan = input("Enter your plan : ")
    if plan == "a":
        clear_terminal()
        set_mark()
    elif plan == 'b':
        clear_terminal()
        add_student()
    elif plan == "c":
        clear_terminal()
        student_info()
    elif plan == "end":
        clear_terminal()
        break