first_letter = input()
second_letter = input()
third_letter = input()
combinations = 0

flag = False
for letter1 in range(ord(first_letter), ord(second_letter)+1):
    for letter2 in range(ord(first_letter), ord(second_letter)+1):
        for letter3 in range(ord(first_letter), ord(second_letter)+1):

            if letter1 != ord(third_letter) and letter2 != ord(third_letter) and letter3 != ord(third_letter):
                print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}", end=" ")
                combinations += 1
print(combinations)





