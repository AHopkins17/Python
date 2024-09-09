# 99 Bottles of Beer on the Wall with while loop

count = 99

while count > 0:
    if count > 1:
        print(count, "bottles of beer on the wall")
        print(count, "bottles of beer")
        print("Take one down, pass it around")

        count = count - 1
        if count > 1:
            print(count, "bottles of beer on the wall\n")
        else:
            print(count, "bottle of beer on the wall!\n")
    else:
        print(count, "bottle of beer on the wall")
        print(count, "bottle of beer")
        print("Take it down, pass it around")
        count = count - 1
        print("No bottles of beer on the wall!\n")