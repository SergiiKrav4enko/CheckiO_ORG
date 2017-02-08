import re
def test_re(text):
    pattern_x = re.compile(text[2])
    result_x = pattern_x.findall(text)
    pattern_y = re.compile(text[4])
    result_y = pattern_y.findall(text)
    if len(result_x)>len(result_y):
        result=result_x
    else:
        result=result_y
    return result
print(test_re("Hello Woooorld!"))