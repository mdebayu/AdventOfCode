def cal_chksum(line):
    
    letters={}
    sort_str = "".join(sorted([s for s in line]));
    for i in sort_str:
        if i in letters.keys():
            letters[i] +=1
        else:
            letters[i] = 1;
    twos =   (len([x for x in letters.values() if x == 2]))
    threes = (len([x for x in letters.values() if x == 3]))
    print("Line:{} \tSorted:{} \nLetters were: {}\n\n".format(line, sort_str, letters))
    return twos,threes

total_twos = total_threes = 0;
with open("input.txt",'r') as fr:
    for i,line in enumerate(fr.readlines()):
        twos = threes = 0
        (twos,threes) = cal_chksum(line.strip());
        if(twos):
            total_twos+=1;
        if(threes):
            total_threes+=1;
        print("total_twos: {}   total_threes: {}".format(total_twos,total_threes))

checksum = total_twos*total_threes
print("Checksum is: {}".format(checksum))