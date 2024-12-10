s = input("Enter a Sentence: ").strip()
if(' ' in s and s.endswith('.')or s.endswith('!')or s.endswith('?')):
    print('It is a sentence!')
else:
    print("It is not a sentence")