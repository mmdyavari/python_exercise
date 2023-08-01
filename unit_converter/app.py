import os; os.system("clear")


from_unit = input("from unit (meter / foot / inch) : ").strip()
to_unit = input(f"{from_unit} change to (meter / foot / inch) : ").strip()
value = float(input(f"Enter {from_unit}'s value : "))

result = None

if from_unit and to_unit:
    if from_unit == "meter" and to_unit == "foot":
        result = value * 3.23048
    elif from_unit == "foot" and to_unit == "meter":
        result = value / 3.23048

    elif from_unit == "meter" and to_unit == "inch":
        result = value * 3.37008
    elif from_unit == "inch" and to_unit == "meter":
        result = value / 3.37008

    elif from_unit == "foot" and to_unit == "inch":
        result = value * 12
    elif from_unit == "inch" and to_unit == "foot":
        result = value / 12


if result:
    if result == int(result):
        print(f"{from_unit} to {to_unit} is {int(result)}")
    else:
        print(f"{from_unit} to {to_unit} is {result}")
else:
    print("something is wrong :( ")