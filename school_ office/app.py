import random

class Office:
    all_students = {}
    
    def __init__(self, f_name, l_name, age, id_card):
        self.f_name = f_name
        self.l_name = l_name
        self.age = str(age)
        self.id_card = str(id_card)
        random.seed(id_card)
        self.stu_id = str(random.randint(11111, 99999))
        info = {'f_name':f_name, 'l_name':l_name, 'age':age, 'id_card':id_card, 'stu_id':self.stu_id }
        Office.all_students.update({id_card : info})


    @classmethod
    def find_stu (cls, id_card_or_stu_code = 0):
        try:
            return Office.all_students[str(id_card_or_stu_code)]
        except:
            for stu in Office.all_students:
                if Office.all_students[stu]["stu_id"] == str(id_card_or_stu_code):
                    return Office.all_students[stu]
            else:
                return "we do not have this user :("

    @classmethod
    def students (cls):
        li = [(i, f"{cls.all_students[i]['f_name']} {cls.all_students[i]['l_name']}") for i in cls.all_students]
        return li


class School_1 (Office):
    def __init__(self, f_name, l_name, age, id_card, birth):
        super().__init__(f_name, l_name, age, id_card)

class School_2 (Office):
    pass



user1 = School_1('mohammad', 'yavarii', 22, 3242339258, "2023,11,2")
user1 = School_2('reza', 'ahmadian', 22, 8647293645)

stus = Office.students()
for i in stus:
    print(i)