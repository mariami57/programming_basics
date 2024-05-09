jury_n = int(input())

input_line = input()
total_counter = 0
total_sum = 0
while input_line != "Finish":
    presentation_name = input_line

    current_counter = 0
    current_sum = 0

    for grade in range(1, jury_n+1):
        current_grade = float(input())
        current_counter += 1
        current_sum += current_grade
    total_counter += current_counter
    total_sum += current_sum

    avg_grade_per_presentation = current_sum / current_counter
    print(f"{presentation_name} - {avg_grade_per_presentation:.2f}.")

    input_line = input()

final_average_grade = total_sum / total_counter
print(f"Student's final assessment is {final_average_grade:.2f}.")


