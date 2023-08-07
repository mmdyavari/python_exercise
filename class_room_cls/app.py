
class Class_room :
    students = []

    def __init__ (self, class_name):
        self.class_name = class_name


    # method for add a student in the class
    def add_student (self, name, family):
        stu = {"name" : name, "family" : family, "group" : self.class_name, "courses" : {}}
        Class_room.students.append(stu)
        print(f"{name} {family} added :)")


    # method for add many courses for this class
    def courses_list (self, *courses):
        if Class_room.students:
            for user in Class_room.students:
                for i in courses:
                    user["courses"].update({i : 0})
            print("courses added :)")
        else:
            print("there is not any student in this class :( please add students first ")


    # set marks for each student
    def student_marks (self, name, family):
        flag = True
        # find user in students
        for user in Class_room.students:
            if user["name"] == name and user["family"] == family and user["group"] == self.class_name:
                flag = False
                # get correct number for each lessons and average
                for i in user['courses'].keys():
                    while True:
                        try :
                            num = float(input(f"{i} : "))
                            user["courses"].update({i:num})
                            break
                        except:
                            print("please Enter number for marks :/")

                # set average 
                av = sum(user['courses'].values()) / len(user['courses'])
                user.update({"average": av})

        # when we don't find user in students run this code 
        if flag:
            print("we don't have this student in this class :(")



    # class method for show all students 
    @classmethod
    def show_students_ino (cls):
        return cls.students
    
