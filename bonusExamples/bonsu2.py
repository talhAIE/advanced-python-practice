# bonus examle 2: try except block
try:
    width=float(input("Enter rectangle width: "))
    length=float(input("Enter rectangle length: "))
    if not width == length:
        area=width*length
        print(area)
    else:
        exit('Square is not allowed')
except ValueError:
    print("Enter only integer value")

