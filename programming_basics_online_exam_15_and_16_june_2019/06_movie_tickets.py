a1 = int(input())
a2 = int(input())
n = int(input())
third_symbol_limit = int(n / 2)
second_symbol = 0
third_symbol = 0
for first_letter in range(a1, a2):
    first_symbol = chr(first_letter)
    fourth_symbol = first_letter
    for second_letter in range(1, n):
        second_symbol = second_letter
        for third_letter in range(1, third_symbol_limit):
            third_symbol = third_letter
            if first_letter % 2 != 0 and (second_symbol + third_symbol + fourth_symbol) % 2 != 0:
                print(f"{first_symbol}-{second_symbol}{third_symbol}{fourth_symbol}")

a1 = int(input())
a2 = int(input())
n = int(input())
third_symbol_limit = int(n / 2)

for first_letter in range(a1, a2):
    i = chr(first_letter)
    l = first_letter
    for j in range (1,n):
        for k in range (1, third_symbol_limit):
            if first_letter % 2 != 0 and (j+k+l) % 2 !=0:
                print(f"{i}-{j}{k}{l}")

