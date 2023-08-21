import random
import requests

key = "api_key"
url = f"https://api.kavenegar.com/v1/{key}/sms/send.json"


# generate validation code
def code_generator (base):
    random.seed(base)
    return random.randint(1111, 9999)

# send code message
def send_message (phone_number, base):
    payload = {
        "receptor" : phone_number, 
        "message" : code_generator(base),    
    }
    result = requests.post(url, data=payload)
    
# validation
def validation (code, base):
    if str(code) == str(code_generator(base)):
        return True
    else:
        return False



if __name__ == "__main__":
    send_message(phone_number = "09036330147", base=10)
    print(validation("1644", 10))

