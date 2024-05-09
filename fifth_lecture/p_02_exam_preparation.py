n_poor_grades = int(input())

task_name = input()

grade_sum = 0
poor_grade_counter = 0
last_task = ""
problems_counter = 0
flag = False

while task_name != "Enough":
    grade = int(input())
    grade_sum += grade
    problems_counter += 1

    if grade <= 4:
        poor_grade_counter += 1

    if poor_grade_counter == n_poor_grades:
        flag = True
        break

    last_task = task_name
    task_name = input()


avg_grade = grade_sum / problems_counter

if flag:
    print(f"You need a break, {poor_grade_counter} poor grades.")

else:
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {problems_counter}")
    print(f"Last problem: {last_task}")



