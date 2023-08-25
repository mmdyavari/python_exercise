import os
import platform

# clear user terminal 
if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

# remove this text in get_code.txt
to_replace = """# write your code here (with indent same this)
# then run python file (app.py)
# ------------------------"""

# read get_user.txt file
with open ("mro_finder/get_code.txt", "r") as file:
    user_code_txt = file.read().replace(to_replace, '').strip()
    which_class = input("which class you want ? ").strip()

try:
    # write user code in python file for get mro
    with open ("mro_finder/user_code.py", "w") as file:
        file.write(f"""
def find_mro ():
    {user_code_txt}
    return {which_class}.mro()
    """)
    
    # run python file for get result (mro)
    import user_code
    class_mro = user_code.find_mro()
    
except:
    # if result is Error
    print("code is not valied :(")

else:
    # show python file result (mro)
    index_counter = 1
    for i in class_mro:
        if str(i) != "<class 'object'>":
            print(f"{index_counter}-{str(i)[36:-2]}")
            index_counter += 1

# clear python file
with open ("mro_finder/user_code.py", "w") as file:
    file.write('')
