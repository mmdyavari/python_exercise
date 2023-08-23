class Name:
    names = []
    def __init__ (self, name):
        Name.names.append(name)

class Family:
    familys = []
    def __init__ (self, family):
        Family.familys.append(family)

class Age:
    ages = []
    def __init__ (self, age):
        Age.ages.append(age)


class Child (Name, Family, Age):
    full_info = []
    def __init__ (self, name, family, age):
        Name.__init__(self, name)
        Family.__init__(self, family)
        Age.__init__(self, age)
        Child.full_info.append([name, family, age])

    def user_info (self):
        return [self.names, self.familys, self.ages]

    @classmethod
    def all_names (cls):
        return cls.names
    
    @classmethod
    def all_familys (cls):
        return cls.familys
    
    @classmethod
    def all_ages (cls):
        return cls.ages
    
    @classmethod
    def all_users (cls):
        return cls.full_info
    

if __name__ == "__main__":
    user1 = Child("korush", "ghanbary", 31)
    user1 = Child("mohammad", "yavarii", 22)

    print(user1.all_names())
    print(user1.all_familys())
    print(user1.all_ages())
    print(user1.all_familys())