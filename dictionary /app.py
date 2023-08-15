import json, os, platform

# function for clear user terminal 
def clear_terminal ():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()


# read json file of dictionary
with open('dictionary /data.json', 'r') as file:
    data = json.load(file)


# find meaning of word
def find_word (word):
    clear_terminal()

    if word in data:
        return data[word]

    elif word.lower() in data:
        return data[word.lower()]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    # handle system when it doesn't exist
    else:
        same = []
        for i in data:
            if i.find(word) == 0:
                same.append(i) 

        if same:
            print("same your word : \n")
            for i in same[:5]:
                print(f'''   {i}''')

            show = input('\nshow more (yes / no) : ')
            if show == "yes":
                return same
            else:
                return ""

    return "I dont have this word :( "  
    

# app handleer 
while True:
    inp = input("Enter the word : ").strip()
    if inp:
        if inp == "end":
            break
        else:
            meaning = find_word(inp)
            if type(meaning) is list:
                index = 1
                for i in meaning:
                    print(f"({index}) ... {i}")
                    index += 1
            else:
                print(meaning)
