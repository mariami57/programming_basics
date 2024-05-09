input_line = input()
total_ticket_counter = 0
standard_count = 0
student_count = 0
kid_count = 0

while input_line != "Finish":
    movie = input_line
    capacity = int(input())
    ticket_counter = 0
    command_line = input()
    while command_line != "End":
        ticket_type = command_line
        ticket_counter += 1
        total_ticket_counter += 1
        if ticket_type == "standard":
            standard_count += 1
        elif ticket_type == "student":
            student_count += 1
        elif ticket_type == "kid":
            kid_count += 1

        if ticket_counter == capacity:
            break

        command_line = input()
    seats_taken_percentage = ticket_counter / capacity * 100
    print(f"{input_line} - {seats_taken_percentage:.2f}% full.")
    input_line = input()

print(f"Total tickets: {total_ticket_counter}")
standard_percentage = standard_count / total_ticket_counter * 100
student_percentage = student_count / total_ticket_counter * 100
kid_percentage = kid_count / total_ticket_counter * 100
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kid_percentage:.2f}% kids tickets.")
