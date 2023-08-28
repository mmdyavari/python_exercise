
class Number:
    def __init__(self, num):
        self.num = num

    def __add__ (self, other):
        return self.num + other.num
    
    def __iadd__ (self, other):
        self.num += other.num
        return self
    
    def __sub__ (self, other):
        return self.num - other.num
    
    def __mul__ (self, other):
        return self.num * other.num
    
    def __truediv__ (self, otreh):
        return self.num / otreh.num
    
    def __pow__ (self, other):
        return self.num ** other.num
    
    def __lt__ (self, other):
        return self.num < other.num
    
    def __gt__ (self, other):
        return self.num > other.num
    
    def __le__ (self, other):
        return self.num <= other.num
    
    def __ge__ (self, other):
        return self.num >= other.num
    
    def __eq__ (self, other):
        return self.num == other.num 
    
    def __ne__ (self, other):
        return self.num != other.num
    

    def __abs__ (self):
        if "-" in str(self.num):
            if "." in str(self.num):
                self.num = float( str(self.num).replace("-", '') )
            else:
                self.num = int( str(self.num).replace("-", '') )
        return self.num


    def __round__ (self, to = 0):
        self.num = round(self.num, to)
        if '.' in str(self.num) and int(str(self.num)[str(self.num).find('.') + 1]) <= 0:
            self.num = int(self.num)

        return self.num
    

    def __call__ (self):
        return self.num


if __name__ == "__main__":
    a = Number(10)
    b = Number(10)
    # print("sum" , a + b)
    # print("mul" , a * b)
    # print("sub" , a - b)
    # print("pow" , a ** b)
    # print("truediv" , a / b)
    # print("lt" , a < b)
    # print("gt" , a > b)
    # print("le" , a <= b)
    # print("ge" , a >= b)
    # print("eq" , a == b)
    # print("ne" , a != b)
    # print("abs", abs(a))
    # print("round", round(a, 3))
    print(a())