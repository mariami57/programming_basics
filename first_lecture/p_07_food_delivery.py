n_chicken_menu = int(input())
n_fish_menu = int(input())
n_veggie_menu = int(input())

cost_chicken_menu = n_chicken_menu * 10.35
cost_fish_menu = n_fish_menu * 12.40
cost_veggie_menu = n_veggie_menu * 8.15

bill_before_desert = cost_chicken_menu + cost_fish_menu + cost_veggie_menu

desert = bill_before_desert * 0.2
delivery = 2.5

total_cost_food = bill_before_desert + desert + delivery

print(total_cost_food)
