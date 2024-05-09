width = int(input())
length = int(input())
number_of_pieces = width * length
input_line = input()
eaten = False

while input_line != "STOP":
    pieces_taken = int(input_line)
    number_of_pieces -= pieces_taken

    if number_of_pieces <= 0:
        eaten = True
        break

    input_line = input()

diff = abs(number_of_pieces)
if eaten:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{number_of_pieces} pieces are left.")