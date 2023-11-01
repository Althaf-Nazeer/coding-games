def number_pyramid():
    height = int(input("Enter the height of the pyramid: "))

    for i in range(1, height + 1):
        print(" " * (height - i), end="")
        for j in range(i, 0, -1):
            print(j, end="")
        for j in range(2, i + 1):
            print(j, end="")
        print()

number_pyramid()
