def get_starting_number():
    number = input("How many bottles of beer on the wall?")
    while not number.isnumeric() or int(number) < 1:
        number = input("How many bottles of beer on the wall?")
    return int(number)

def sing(starting_number):
    for bottles in range(starting_number, 0, -1):
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
        elif bottles == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down, pass it around, 1 bottle of beer on the wall.")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.\nTake one down, pass it around, {bottles - 1} bottles of beer on the wall.")