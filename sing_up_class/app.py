import string
import random

class Sing_Up:
    __ids = []
    __users = []

    # dunder init
    def __init__ (self, username, password):
        self.__id = self.__code_generator(length=8, is_id=True)
        self.__username = username
        self.__password = password
        Sing_Up.__users.append({'id':self.__id, "username":self.__username, "password":self.__password})

    # code generator function for id and validation code
    @staticmethod
    def __code_generator (length = 5, is_id = False):
        if is_id:
            letters = list(string.ascii_letters + string.digits)
            random.shuffle(letters)
            while True:
                code = "".join(random.choices(letters, k=length))
                if code not in Sing_Up.__ids :
                    Sing_Up.__ids.append(code)
                    return code
        return "".join(random.choices(list(string.digits), k=length))

    
    # id getter
    @property
    def id (self):
        return self.__id

    # username getter
    @property
    def username (self):
        return self.__username

    # change username (username setter)
    @username.setter
    def username (self, new):
        code = Sing_Up.__code_generator()
        valid = input(f"{code} : ")
        if valid == code:
            self.__username = new
        else:
            print("code is not valied :(")

    # password getter
    @property
    def password (self):
        code = Sing_Up.__code_generator()
        valid = input(f"{code} : ")
        if valid == code:
            return self.__password
        else:
            print("code is not valied :(")
        return self.__password

    # change password (password settr)
    @password.setter
    def password (self, new):
        code = Sing_Up.__code_generator()
        valid = input(f"{code} : ")
        if valid == code:
            self.__password = new
        else:
            print("code is not valied :(")

    # get all users info
    @classmethod
    @property
    def users (cls):
        return Sing_Up.__users



if __name__ == "__main__":
    user = Sing_Up("Mmd_yavarii", "mmd12345")