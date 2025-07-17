# bonus example 4: 
feet_inches=input("Enter feet and inches: ")

def convert(feet_inches):
    parts=feet_inches.split(" ") # split the string into a list
    feet=float(parts[0])
    inches=float(parts[1])

    meters=feet*0.3048+inches*0.0254
    return f"{meters} meters"

print(convert(feet_inches))