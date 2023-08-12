class Math:
    # attributs
    PI = 3.14159265359
    E = 2.718281828459045
    LN10 = 2.30258509299
    LN2 = 0.69314718056
    LOG10E = 0.4342944819
    LOG2E = 1.44269504089
    SQRT1_2 = 0.7071067811865476
    SQRT2 = 1.41421356237 

    @staticmethod
    def abs (num):
        to_str = str(num).replace('-', '')
        if "." in to_str:
            return float(to_str)
        else:
            return int(to_str)

    @staticmethod
    def min (*args):
        minim = args[0]
        for i in args:
            if  i<minim:
                minim = i
        return minim
    
    @staticmethod
    def max (*args):
        maxim = 0
        for i in args:
            if i>maxim :
                maxim = i
        return maxim

    @staticmethod
    def pow (num1 , num2):
        res = 1
        for i in range(num2):
            res *= num1
        return res
    
    @staticmethod
    def round (num):
        return round(num)

    @staticmethod
    def floor (num):
        if type(num) is float:
            rounder = round(num)
            if rounder > num:
                return rounder -1
            else:
                return rounder
        return num


    @staticmethod
    def ceil (num):
        if type(num) is float:
            rounder = round(num)
            if rounder > num:
                return rounder
            else:
                return rounder + 1
        return num



if __name__ == "__main__":
    pass
    # print(Math.abs(-2.3947))
    # print(Math.ceil(11.1))
    # print(Math.min(2, 10, 11, -1, 19))
    # print(Math.max(1, 2, 1, -1, -100, 21))
    # print(Math.pow(2, 4))
    # print(Math.round(12.84638468))
    # print(Math.floor(1.9))
    # print(Math.random())
