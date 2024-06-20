def get_starting_number():
    while True:
        bottles = input("How many bottles of beer on the wall? ")
        if bottles.isdigit() and int(bottles) >= 1:
            return int(bottles)

def sing(starting_bottles):
    bottles = starting_bottles
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles-1} {'bottle' if bottles-1 == 1 else 'bottles'} of beer on the wall.\n")
        else:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        bottles -= 1