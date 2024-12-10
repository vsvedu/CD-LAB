p = input("Enter a parragraph: ").strip()
if len(p) > 1 and ' ' in p:
    if p[-1] in ['\t','\n','.','!','?']:
        print("It is a paragraph")
    else:
        print("It is not a paragraph")
else:
    print("Given input is not a Paragraph!")