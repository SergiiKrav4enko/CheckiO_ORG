def checkio(text):
    lst = [let for let in text.lower() if let.isalpha()]
    lst.sort()
    counter = [lst.count(elem) for elem in lst]
    freq_let = lst[counter.index(max(counter))]
    return freq_let
print(checkio("How do you do?"))