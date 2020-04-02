
Height = int(input("Enter the height = "))

print(Height)
counter = 1
while Height > 0:

    for x in range(Height-1):
        print(" ", end="")

    for x in range(counter):
        print("#", end="")

    print("  ", end="")

    for x in range(counter):
        print("#", end="")

    counter = counter+1
    print("\n")
    Height = Height-1
