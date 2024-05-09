input_line = input()
best_word = ""
best_word_ascii = 0
while input_line != "End of words":
    ascii_value = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'Y', 'I', 'O', 'U']
    for letter in input_line:
        ascii_value += ord(letter)
    if input_line[0] in vowels:
        ascii_value *= len(input_line)
    else:
        ascii_value //= len(input_line)

    if ascii_value > best_word_ascii:
        best_word = input_line
        best_word_ascii = ascii_value
    input_line = input()

print(f"The most powerful word is {best_word} - {best_word_ascii}" )
