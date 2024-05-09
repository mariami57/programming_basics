packaging_paper_n = int(input())
clothing_n = int(input())
glue_liters = float(input())
discount_percentage = int(input())

packaging_paper_price = packaging_paper_n * 5.8
clothing_price = clothing_n * 7.2
glue_price = glue_liters * 1.2

total_cost = packaging_paper_price + clothing_price + glue_price

cost_after_discount = total_cost - (total_cost * discount_percentage / 100)

print(f"{cost_after_discount:.3f}")