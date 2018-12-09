freqList = []; freqSum = [0]; total = 0;
repeats =0; found = False; MAX_REPEATS =250
import time;

with open("input.txt",'r') as fr:
    for it,line in enumerate(fr.readlines()):
        next_num = int(line)
        freqList.append( (next_num))
        total +=next_num;
        print("Repts: {} Iter: {} Number: {} Sum: {}".format(repeats,it,next_num,total))
        if total in freqSum:
            print("Found - Iter: {} Number: {} Sum: {}".format(it,next_num,total))
            found = True
            break;        
        freqSum.append(total)


while(not(found) and repeats <MAX_REPEATS):
    repeats +=1
    print("NOT FOUND REPEATING: {}".format(repeats))
    for it,next_num in enumerate(freqList):
        total+=next_num
        print("Repts: {} Iter: {} Number: {} Sum: {}".format(repeats,it,next_num,total))
        if total in freqSum:
            print("Found - Iter: {} Number: {} Sum: {} Loc:{}".format(it,next_num,total,freqSum.index(total)))
            found = True
            break;        
        freqSum.append(total)

