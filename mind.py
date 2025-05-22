
import random

x2= 400/3                                            
x3= (400/3)*2 +8
                                                                      
list_all_lins=  [
    [(0,0), (x2,x2), (x3,x3)],
    [(0,x3), (x2,x2), (x3,0)],      # دوتا اریب 
    [(x2,0), (x2,x2), (x2,x3)], 
    [(0,x2), (x2,x2), (x3,x2)],     # دو تا به اضافه
    [(0,0), (x2,0), (x3,0)], 
    [(x3,0), (x3,x2), (x3,x3)], 
    [(x3,x3), (x2,x3), (0,x3)], 
    [(0,x3), (0,x2), (0,0)]          # چهار تا اطراف
                ]


def first_step(empty_loc):
    next_step = None

    list_goshe=[(0,0) , (0,x3) , (x3,0) , (x3,x3)]
    list_goshe_mojod=list(filter(lambda x : x in empty_loc, list_goshe))
    # print('goshe',list_goshe_mojod)

    if (x2,x2) in empty_loc:
        next_step=(x2,x2)
        
        print(11)
        # return next_step

    else:
        

        if list_goshe_mojod !=[]:
            next_step= random.choice(list_goshe_mojod)
            
        elif empty_loc !=[]:
            next_step= random.choice(empty_loc)
            # print(1)
            print(23)

    if next_step:

        return next_step
    print(33)




def attack_or_defend(list_game , empty_loc): 
    for line in list_all_lins:
        count=0
        for item in line:
            if item in list_game:
                count+=1

            else:
                next_step= item
        if count == 2 and next_step in empty_loc:
            return next_step
            break
