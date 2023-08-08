import os, pickle, json, string, random, platform, time

# function for turn of each system 
def shutdowner ():
    sys = platform.system()
    if sys == "Windows":
        os.system('shutdown /s')
    else:
        os.system("sudo shutdown -h now")


class Asistant :
    # password generator 
    def pass_generator (self, length = 8):
        chars = list(string.ascii_letters + string.digits + string.punctuation)
        random.shuffle(chars)
        return "".join(random.choices(chars, k=length))


    # chaptcha code generator 
    def captcha_generator (self, length = 5):
        chars_num = list(string.digits * 10)
        chars_upper = string.ascii_uppercase
        chars_lower = string.ascii_lowercase
        username = random.choice(chars_upper) + random.choice(chars_lower)
        random.shuffle(chars_num)
        for i in chars_num:
            username += i
        return username[:length]


    # json converter
    def json_converter (self, data = None):
        return json.dumps(data, indent=4)


    # pickle converter
    def pickle_converter (self, data = None):
        return pickle.dumps(data)


    # turn off the computer with timer
    def timer_turn_of (self, hour = 0 , minut = 0, second = 0):
        sec = second + (minut * 60) + (hour * 3600)
        for i in range(sec, 0, -1):
            os.system('clear')
            print(f'{i} - second')
            time.sleep(1)
        else:
            print("Shut down :)")
            shutdowner()


    # turn off with on time 
    def turn_of_on_time (self, hour = 0, minut = 0, second = 0):
        """hour is 24/H"""
        if hour or minut or second:
            os.system("clear")
            print(f"shut down at {hour}:{minut}:{second}")
            now = time.localtime()
            time_for_turn_of = (now.tm_year, now.tm_mon, now.tm_mday, hour, minut, second, now.tm_wday, now.tm_yday, now.tm_isdst)
            time_for_sleep = time.mktime(time_for_turn_of) - time.mktime(now)

            if time_for_sleep > 0 :
                time.sleep(time_for_sleep)
                print("Shut down :)")
                shutdowner()

if __name__ == "__main__":
    test = Asistant()
    # print(test.pass_generator())
    # print(test.captcha_generator())
    # print(test.json_converter(True))
    # print(test.pickle_converter(True))
    # test.timer_turn_of(second=5)
    # test.turn_of_on_time(15,52)
