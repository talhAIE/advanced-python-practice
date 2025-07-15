content=['I am learning python' ,"I am learning ai agents" ,"i am learning english"]
filenames=['first.txt','second.txt','third.txt']

for i in range(len(filenames)):
    file=open(filenames[i],'w')
    file.write(content[i])
    file.close()

for i in range(len(filenames)):
    with open(filenames[i],'r') as file:
        print(file.read())
