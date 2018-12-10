##Make massive 2d array
## fill with id on each new line. 
##if there is a conflict increment conflict
## Fill location with x

import re
import numpy as np
conflict_count=0;
def main():
    MAX_ROWS = 1024; MAX_COLS = 1024;
    board = np.zeros((MAX_ROWS,MAX_COLS))
    goodlist = []
    with open("input.txt",'r') as fr:
        for line in fr.readlines():
            id_,xloc,yloc,wid,lng = get_claim(line)
            #id_,xloc,yloc,wid,lng = get_claim("#123 @ 3,2: 5x4")
            goodlist.append(id_)
            board,goodlist = fillboard(id_,xloc,yloc,wid,lng,board,goodlist)
            print(np.count_nonzero(board==0.5))
            print("GoodList:{}".format(goodlist))
    
    
def fillboard(id_,x,y,wid,lng,board,goodlist):
    #print("id: {} x:{} y:{} wid:{} len:{}".format(id_,x,y,wid,lng))
    for i in range(x,x+wid):
        for j in range (y,y+lng):
            #print("id:{} i:{} j:{} val:{}".format(id_,i,j,board[j][i]))
            if board[j][i] ==0:
                board[j][i] = id_;
            else:
                if id_ in goodlist:
                        print("GoodList:{} Removed: {}".format(goodlist,board[j][i]))
                        goodlist.remove(id_)
                if board[j][i] != 0.5:
                    if int(board[j][i]) in goodlist:
                        print("GoodList:{} Removed: {}".format(goodlist,id_))
                        goodlist.remove(int(board[j][i]))

                else:
                    board[j][i] = 0.5;

                
                
 
                
                
                
                
    return board,goodlist    
        
def get_claim(claim_str):
    line = claim_str.split(" ");
    #form ="#<claim_id> @ <xloc>,<yloc>: <width>x<length>"
    srchr =re.split("(\d+)",claim_str)
    return(int(srchr[1]),int(srchr[3]),int(srchr[5]),int(srchr[7]),int(srchr[9]))    
#return {"id":int(srchr[1]), 
     #       "xloc":int(srchr[3]), 
      #      "yloc":int(srchr[5]),
       #     "width":int(srchr[7]),
        #    "length":int(srchr[9])}
    
    
if __name__ == "__main__":
    main()