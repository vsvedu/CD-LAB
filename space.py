p = input("Enter Sentence's: ")
c = 0
for i in p:
    if i == ' ':
        if p[-1] in ['.','!','?']:
            c += 1
    else:
        ("Enter Valid Sentence!")
print(c)