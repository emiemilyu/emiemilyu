word=input('Enter a word')
new_word=''
for x in word:
    new_word+=str(ord(x))
print(new_word)