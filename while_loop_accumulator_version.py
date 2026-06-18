def get_starting_number():
    number = input("How many bottles of beer on the wall?")
    while not number.isnumeric() or int(number) < 1:
        number = input("How many bottles of beer on the wall?")
    return int(number)

def sing(starting_number):
    i = starting_number
    while i >= 1:
        if i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
        elif i == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down, pass it around, 1 bottle of beer on the wall.")
        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down, pass it around, {i - 1} bottles of beer on the wall.")
        i = i - 1