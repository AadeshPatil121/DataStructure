

def move_to_pos(pos) :
    """ pos = 10  position = [5,5]"""
    ques = pos // 4
    rems = pos % 4
    if rems == 0 :
        position = (ques,4)
    else :
        position = (ques+1,rems)
    return  position


def pos_to_move(pos) :
    news = 4 * (pos[0] - 1)
    news = news + pos[1]
    return news


def check_legal_move(pos) :
    if pos[0] > 0 and pos[0] < 4 :
        if pos[1] > 0 and pos[1] < 5 :
            return  True
        else :
            return  False
    else:
        return False


def all_routes(pos) :
    lists = []
    operations = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
    for x in operations :
        ans = [x[0]+pos[0],x[1]+pos[1]]
        a = check_legal_move(ans)
        if a == True :
            lists.append(ans)
    k = []
    for x in lists :
        k.append(pos_to_move(x))
    return k

