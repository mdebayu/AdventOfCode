def common_letters(word1,word2):
    letters = []
    for x in word1:
        if x in word2:
            letters.append(x)
        else: 
            print("Differing Letter: {}".format(x))
    return "".join(letters)

box_ids = []        
with open("input.txt",'r') as fr:
    for line in fr.readlines():
        box_ids.append(line.strip())

for box_id_iter, box_id in enumerate(box_ids):
    for check in box_ids[box_id_iter:len(box_ids)]:
        if len(box_id)==len(check):
            one_mistake =False;
            for letter_iter,letter in enumerate(box_id):
                if letter ==check[letter_iter]:
                    continue;
                else:
                    
                    if (one_mistake):
                        one_mistake=False;
                        break;
                    else:
                        one_mistake=True;
            else:
                if (one_mistake):
                    print ("Words are:   {}   {}".format(box_id,check))
                    print("Common Letters: {}".format(common_letters(box_id,check)))
                else:
                    continue
        
