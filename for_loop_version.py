def get_starting_number():
    while True:
        bottles = input("How many bottles of beer on the wall? ")
        if bottles.isnumeric() and int(bottles) >= 1:
            return int(bottles)

def sing(bottles):
    for i in range(bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} {'bottle' if i-1 == 1 else 'bottles'} of beer on the wall.\n")
        else:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")

