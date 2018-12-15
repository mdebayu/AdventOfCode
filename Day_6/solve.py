
import itertools
import numpy as np;
import time
MAX_COL = 350; MAX_ROW= 350;
def main():
    file=[];
    with open("input.txt") as fileread:
        for l in fileread.readlines():
            file.append( "-".join(l.strip().split(', '))  )
    
    
    board=[" # " for i in range(MAX_COL*MAX_ROW)]
    a= time.clock()
    for i in range(MAX_ROW):
        print("Row:{} of {}".format(i,MAX_ROW))
        for j in range(MAX_COL):            
            if j%35 ==0:
                print("COL:{}  Time Past:{}".format(i,time.clock() -a))
            find_pt((j,i),file,board);
    
    #print(np.array(board,dtype=object).reshape((MAX_COL,MAX_ROW)))
    uniques ={}
        
    max_val =["",0];
    for i in board:
        if i in uniques:
            uniques[i] = uniques[i]+1
            if uniques[i] >max_val[1]:
                max_val[0] = i;
                max_val[1] = uniques[i];
            
        else:
            uniques.update({i:1})
    
    print("Unique List: \n{}".format(uniques))
    
    print("MaxVal:{}\tMaxCount:{}".format(max_val[0],max_val[1]))
    
def find_pt(start,points,board):
    cur_sqrs= [start]
    to_visit=[]
    visited  =[]
    
    for i in range(10):
        to_visit = next_visits(cur_sqrs,visited)
        match = list((filter(lambda sqr: "{}-{}".format(sqr[0],sqr[1]) in points, cur_sqrs)))
        match = delete_rpts(match)
        
        # if one match
        if len(match) == 1:
            board[start[0]+start[1]*MAX_COL] = "{}-{}".format(match[0][0],match[0][1])
        else:
            if len(match) > 1:
                board[start[0]+start[1]*MAX_COL] = " . "
            else:
                # else
                visited += ["{}-{}".format(x[0],x[1]) for x in cur_sqrs]
                cur_sqrs = to_visit

def next_visits(cur_sqrs,visited):
    to_visit =[]
    
    for sqr in cur_sqrs:
        if (sqr[0]<MAX_COL-1):
            to_visit.append([sqr[0] + 1,sqr[1]])
        if (sqr[0]>0):
            to_visit.append([sqr[0] - 1,sqr[1]])
        if (sqr[1]<MAX_ROW-1):
            to_visit.append([sqr[0],sqr[1] + 1])
        if (sqr[1]>0):
            to_visit.append([sqr[0],sqr[1] - 1])
    return(list(filter(lambda sqr: "{}-{}".format(sqr[0],sqr[1])not in visited,to_visit)))

def delete_rpts(match):
    a = time.clock();
    for it, i in enumerate(match):
        for j in match[it+1:]:
            if i == j:
                del match[it]
    print(time.clock()-a)
    return match


    
if __name__ == "__main__":
    #main() 
    #[print(x) for x in next_visits([[5,5]],["5-6"])]
    #find_pt([3,1],["5-1","2-1"],[])
    
    l = 
    print(delete_rpts(l))
    a=time.clock();
    print(set(l))
    print(time.clock()-a)