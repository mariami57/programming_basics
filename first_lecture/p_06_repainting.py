nylon_sq_m = int(input())
paint_litres = int(input())
diluter_litres = int(input())
hours_workers = int(input())

nylon_cost = (nylon_sq_m * 1.5) + 3

paint_total_litres = paint_litres + (paint_litres * 0.1)
paint_cost = paint_total_litres * 14.5

diluter_cost = diluter_litres * 5

bags = 0.4

total_cost_materials = (nylon_cost + paint_cost + bags + diluter_cost)

one_hour_workers = 0.3 * (nylon_cost + paint_cost + bags + diluter_cost)

total_cost_workers = one_hour_workers * hours_workers

overall_cost_with_work = total_cost_materials + total_cost_workers

print(overall_cost_with_work)






