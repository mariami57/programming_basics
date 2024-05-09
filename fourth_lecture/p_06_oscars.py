actor_name = input()
points = float(input())
reviewers_n = int(input())


diff = 0

for _ in range(reviewers_n):
    reviewer_name = input()
    reviewer_points = float(input())

    total_reviewer_points = (len(reviewer_name)*reviewer_points) /2
    points += total_reviewer_points

    diff = abs(points - 1250.5)

    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break


else:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")

