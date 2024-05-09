volume_litres = int(input())
p1_debit = int(input())
p2_debit = int(input())
hours = float(input())

p1 = p1_debit * hours
p2 = p2_debit * hours

total = p1 + p2
percentage_full = total / volume_litres * 100
p1_percentage = p1 / total * 100
p2_percentage = p2 / total * 100

diff = abs((volume_litres - total))
if total > volume_litres:
    print(f"For {hours:.2f} hours the pool overflows with {diff:.2f} liters.")
else:
    print(f"The pool is {percentage_full:.2f}% full. Pipe 1: {p1_percentage:.2f}%. Pipe 2: {p2_percentage:.2f}%.")
