running_sum = 0;
with open("input.txt",'r') as fr:
    for line in fr.readlines():
        running_sum += (int(line))
        print("Value: {}   Current_Sum = {}".format(int(line),running_sum))
print("\n\n\nTotal sum: {}\n".format(running_sum))