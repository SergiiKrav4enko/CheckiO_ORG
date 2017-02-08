def checkio (data):
    result=False
    result_data=[False, False, False, False]
    num_data='1234567890'
    ch_data='QWERTYUIOPASDFGHJKLZXCVBNM'
    ch_mini_data='qwertyuiopasdfghjklzxcvbnm'
    if len(data)>9:
        result_data.pop(0)
        result_data.insert(0, True)
    for i in range(len(num_data)):
        if num_data[i] in data:
            result_data.pop(1)
            result_data.insert(1, True)
            break
    for i in range(len(ch_data)):
        if ch_data[i] in data:
            result_data.pop(2)
            result_data.insert(2, True)
            break
    for i in range(len(ch_mini_data)):
        if ch_mini_data[i] in data:
            result_data.pop(3)
            result_data.insert(3, True)
            break
    if False in result_data:
        result=False
    else:
        result=True
    print(len(data))
    print(result_data)
    return result
print(checkio ('sfhjksdiAjksl2'))