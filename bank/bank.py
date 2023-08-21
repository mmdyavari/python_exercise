import random
import send_sms
import time

class Bank :
    all_users = {}

    def __init__ (self, f_name, l_name, id_card, password):
        if  str(id_card) in Bank.all_users.keys():
            raise ValueError ("you have aan acount here please log in ")
        else:
            # create user attibuts
            self.f_name = f_name
            self.l_name = l_name
            self.id_card = str(id_card)
            self.password = str(password)
            random.seed(self.id_card)
            self.bank_number = str(random.randint(111111111111, 999999999999))            
            # add user in users
            Bank.all_users.update({str(id_card) : {'f_name':f_name, "l_name":l_name, "bank_number": self.bank_number , "password":str(password), "inventory":0, "history": []}})
        

    # user information
    def info (self):
        user = Bank.all_users[self.id_card]
        return user


    # get inventory of user 
    def inventory (self):
        user = Bank.all_users[self.id_card]
        return user["inventory"]


    # pay mony
    def pay (self, value):
        user = Bank.all_users[self.id_card]
        if user["inventory"] > value:
            info = {"date":time.ctime(), "model":"pay", "value":value}
            user["history"].append(info)
            user.update({"inventory" : user["inventory"] - value})

        else:
            raise ValueError ("You don't have that much money")


    # receive mony
    def receive (self, value):
        user = Bank.all_users[self.id_card]
        info = {"date":time.ctime(), "model":"receive", "value":value}
        user["history"].append(info)
        user.update({"inventory" : user["inventory"] + value})


    # show history of payments
    def history (self):
        user = Bank.all_users[self.id_card]
        return user["history"]


    # money transfer
    def transfer (self, bank_number, value):
        receiver = ''
        me = Bank.all_users[self.id_card]
        # find receiver
        for i in Bank.all_users:
            if Bank.all_users[i]["bank_number"] == str(bank_number):
                receiver = Bank.all_users[i]
                break
        # get permission
        if receiver:
            if me["inventory"] > value:
                permission = input(f"{receiver['f_name']} {receiver['l_name']} yes or no ? ")
                # money exchange
                if permission.strip() == "yes":
                    # add money to the recipient
                    receiver.update({"inventory" : receiver["inventory"] + value})
                    info = {"date":time.ctime(), "model":"receive_exchange", "value":value}
                    receiver['history'].append(info)
                    # deduction of money from the sender
                    me.update({"inventory" : me["inventory"] - value})
                    info = {"date":time.ctime(), "model":"pay_exchange", "value":value}
                    me['history'].append(info)
        else:
            print("we do not have this user :(")


    # method for log in user
    @classmethod
    def login (cls, id_card, password):
        try:
            user_info = Bank.all_users[str(id_card)]
            if user_info["password"] == str(password):
                return "log in :)"
        except:
            return 'we dont have this user'


    # method for forget password
    @classmethod
    def forget_password (cls, id_card, phone_number):
        if str(id_card) in Bank.all_users:
            ra = random.random()
            send_sms.send_message(phone_number, ra)
            code = input("Enter code : ")
            result = send_sms.validation(code, ra)
            return result
        else:
            raise ValueError ("you d not have acount :(")

                        


if __name__ == "__main__":
    # user1 = Bank("mohammad", 'yavarii', 123456, "mmd12345")
    # user2 = Bank("reza", 'ahmadian', 123987, "gfds880ds")
    # print(Bank.forget_password(123456, "09036330147"))
    # user1.inventory()
    # user1.receive(130)
    # user1.receive(430)
    # user1.pay(10)
    # a = user1.history()
    # print("-----------------")
    # print(user1.inventory())
    # user1.transfer(473648018937, 100)
    # print(user1.inventory())
    pass