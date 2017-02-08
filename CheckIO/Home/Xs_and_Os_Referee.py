def checkio(game_result):
    result_x1 = game_result[0]
    result_x2 = game_result[1]
    result_x3 = game_result[2]
    result_list={}
    if (result_x1[0] == result_x2[0] and result_x1[0] == result_x3[0]) or (result_x1[0] == result_x1[1] and result_x1[0] == result_x1[2]) or (result_x1[0] == result_x2[1] and result_x1[0] == result_x3[2]):
        if result_x1[0]!='.':
            result_list[True]=result_x1[0]
        else:
            result_list[False] = result_x1[0]
    if (result_x1[1] == result_x2[1] and result_x1[1] == result_x3[1]) or (result_x2[0] == result_x2[1] and result_x2[0] == result_x2[2]):
        if result_x2[1]!='.':
            result_list[True] = result_x2[1]
        else:
            result_list[False] = result_x2[1]
    if (result_x1[2] == result_x2[2] and result_x1[2] == result_x3[2]) or (result_x3[0] == result_x3[1] and result_x3[0] == result_x3[2]):
        if result_x3[2]!='.':
            result_list[True] = result_x3[2]
        else:
            result_list[False] = result_x3[2]
    if result_x1[2] == result_x2[1] and result_x1[2] == result_x3[0]:
        if result_x1[2] != '.':
            result_list[True] = result_x1[2]
        else:
            result_list[False] = result_x1[2]
    if True in result_list:
        result=result_list.get(True)
    else:
        result='D'
    return result
print(checkio(["...","XXX",".XO"]))