# bonus example 3

def get_average(file_path='bonusExamples/temperatures.txt'):
    with open(file_path,'r') as file_local:
        data=file_local.readlines()[1:]
        values =[float(value) for value in data]
        average=sum(values)/len(values)

    return average

print(f"Average temperature: {get_average()}")
