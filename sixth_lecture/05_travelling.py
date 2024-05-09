destination = input()

while destination != "End":
    min_budget = float(input())
    total_savings = 0
    while total_savings < min_budget:
        current_sum = float(input())
        total_savings += current_sum

    print(f"Going to {destination}!")

    destination = input()