# bonus example 5 
feet_inches=input("Enter feet and inches: ")
def parse(feet_inches):
    parts=feet_inches.split(" ") # split the string into a list
    feet=float(parts[0])
    inches=float(parts[1])
    return feet,inches

def convert(feet,inches):
    meters=feet*0.3048+inches*0.0254
    return f"{meters} meters"

# check=parse(feet_inches)
# print(check)
f,i=parse(feet_inches)
result=convert(f,i)
print(result)

# till 13