sq_m_ladscaping = float(input())

landscaping_cost = sq_m_ladscaping * 7.61

discount = landscaping_cost * 0.18
cost_after_discount = landscaping_cost - discount

print(f"The final price is: {cost_after_discount} lv.")
print(f"The discount is: {discount} lv.")