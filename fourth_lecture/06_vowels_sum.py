word = input()

result = 0
for character in word:
    if character == "a":
        result += 1
    elif character == "e":
        result += 2
    elif character == "i":
        result += 3
    elif character == "o":
        result += 4
    elif character == "u":
        result += 5
print(result)