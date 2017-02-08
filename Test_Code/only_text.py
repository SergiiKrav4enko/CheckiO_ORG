text_lower='Lorem ipsum dolor sit amet'
text_sign = ' !/.,+-=?'
text=''
for i in range(len(text_lower)):
    if text_lower[i] not in text_sign:
        text+=text_lower[i]
print(text)
print(len(text))
print(len(text_lower))