word = str(input())
new_word = ''
for char in word:
    if char.isupper() == True:
        new_char = char.lower()
        new_word += new_char
    else:
        new_char = char.upper()
        new_word += new_char

print(new_word)