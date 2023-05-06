import string


alphabet=list(string.ascii_lowercase)
print(alphabet)
word="hello"
for i in word:
    print (alphabet.index(i))
