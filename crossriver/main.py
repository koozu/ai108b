import copy  # 使用深複製
state = [0, 0, 0, 0]  # 人、狼、羊、甘藍菜
nextstate = [0, 0, 0, 0]
fullpath = [[0, 0, 0, 0]]


def move():
    global state, nextstate, fullpath
    ship = 1
    nextstate[0] = 0 if state[0] == 1 else 1
    for i in range(1, 4):
        if state[i] == state[0] and ship < 2:  # 跟人同岸且船還沒坐滿兩個
            nextstate[i] = 0 if state[i] == 1 else 1
            ship += 1
        else:
            #print("can't move")
            continue
        if isvisited():
            #print(str(i) + ":" + str(nextstate) + "isvisited")
            ship = 1
            nextstate[i] = state[i]
        else:
            if isdead():
                #print(str(i) + ":" + str(nextstate) + "isdead")
                ship = 1
                nextstate[i] = state[i]
            else:
                break
    temp = copy.deepcopy(nextstate)
    state = temp
    fullpath.append(temp)
    #print("path:" + (str)(fullpath))


def isvisited():
    global nextstate, fullpath
    for path in fullpath:
        if nextstate == path:
            #print("nextstate:" + (str)(nextstate) + "\tpath:" + (str)(p))
            return True
    return False


def isdead():
    global nextstate
    if nextstate[1] == nextstate[2] and nextstate[2] != nextstate[0]:
        return True
    elif nextstate[2] == nextstate[3] and nextstate[2] != nextstate[0]:
        return True
    return False


def checksuccess():
    global state
    if state[0] == 1 and state[1] == 1 and state[2] == 1 and state[3] == 1:
        return True
    return False


def main():
    global fullpath
    while True:
        #input()
        if checksuccess():
            break
        else:
            move()
    print("path:")
    for path in fullpath:
        print("\t" + str(path))


main()
