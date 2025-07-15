# bonus examle 1: Password strong or weak

# user_password=input("Enter your password: ")

# result={}
# if len(user_password)>=8:
#     result['length']=True
# else:
#     result['length']=False

# digit=False
# for i in user_password:
#     if i.isdigit():
#         digit=True

# result['digit']=digit

# uppercase=False
# for i in user_password:
#     if i.isupper():
#         uppercase=True
# result['uppercase']=uppercase

# if all(result.values()):
#     print(result)
#     print("Strong password")
# else:
#     print(result)
#     print('Weak Password')
# new concept i learn here is all() function

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