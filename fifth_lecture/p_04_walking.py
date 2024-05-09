input_line = input()
steps_counter = 0
goal = 10000

while input_line != "Going home":
    n_steps = int(input_line)
    steps_counter += n_steps

    if steps_counter >= goal:
        break

    input_line = input()

if input_line == "Going home":
    steps_home = int(input())
    steps_counter += steps_home

diff = abs(goal - steps_counter)

if steps_counter >= goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
