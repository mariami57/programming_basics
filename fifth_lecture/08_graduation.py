student_name = input()
years_counter = 0
grade_sum = 0
failed_counter = 0

while True:
    grade = float(input())

    if grade < 4:
        failed_counter += 1

        if failed_counter > 1:
            current_year = years_counter + 1
            print(f"{student_name} has been excluded at {current_year} grade")
            break

        continue

    else:
        years_counter += 1
        grade_sum += grade

    if years_counter == 12:
        average_grade = grade_sum / 12
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
        break

