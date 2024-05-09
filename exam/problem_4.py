days_n = int(input())
quantity_sum = 0
degrees_sum = 0
for day in range(days_n):
    current_quantity = float(input())
    quantity_sum += current_quantity
    current_degrees = float(input())
    degrees_per_day = current_degrees * current_quantity
    degrees_sum += degrees_per_day

avg_degrees = degrees_sum / quantity_sum
print(f"Liter: {quantity_sum:.2f}")
print(f"Degrees: {avg_degrees:.2f}")

if avg_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= avg_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")


