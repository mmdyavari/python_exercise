import random
import string

class Bank:
    __ids = [] 

    # random code generator 
    @staticmethod
    def __id_creator (length = 5, with_upper = True):
        if with_upper:
            letters = list(string.digits + string.ascii_letters)
        else:
            letters = list(string.digits + string.ascii_lowercase)

        random.shuffle(letters)
        return "".join(random.choices(letters, k=length))


    def __init__ (self, name, family, mojodi, password):
        self.__name = name
        self.__family = family
        self.__mojodi = mojodi
        self.__password = password
        while True:
            self.__id = self.__id_creator()
            if self.__id not in Bank.__ids:
                Bank.__ids.append(self.__id)
                break

    # return user information
    def info (self):
        data = {
            "full_name" : f'{self.__name} {self.__family}',
            "bank_id" : self.__id, 
            "password" : self.__password,
            "mojodi" : self.__mojodi
        }
        return data
    
    # get mojodi with call object
    def __call__ (self):
        return self.__mojodi
    
    # buy
    def __add__ (self, other):
        self.__mojodi += other

    # sell
    def __sub__ (self, other):
        self.__mojodi -= other

    # change password
    def change_password (self, old, new):
        valid_code = Bank.__id_creator(4, False)
        validation = input(f"{valid_code} : ")

        if old == self.__password and validation == str(valid_code):
            self.__password = new
        else:
            print("something is wring :)")

    # change name and family
    def change_name (self, name, family):
        valid_code = Bank.__id_creator(4, False)
        validation = input(f"{valid_code} : ")

        if validation == str(valid_code):
            self.__name = name
            self.__family = family
        else:
            print("something is wring :)")



if __name__ == "__main__":
    # user = Bank("mohammad", 'yavari', 0, "m123456")

    # user + 100 
    # user - 19 
    # user()

    # user.change_name('mmd', "yavr")
    # user.change_password("m123456", "mmd1234")

    # user.info()
    pass