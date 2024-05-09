country = input()
item = input()

score = 0
if country == "Russia":
    if item == "ribbon":
        score = 9.100 + 9.400
    elif item == "hoop":
        score = 9.300 + 9.800
    if item == "rope":
        score = 9.600 + 9.000

elif country == "Bulgaria":
    if item == "ribbon":
        score = 9.600 + 9.400
    elif item == "hoop":
        score = 9.550 + 9.750
    if item == "rope":
        score = 9.500 + 9.400

if country == "Italy":
    if item == "ribbon":
        score = 9.200 + 9.500
    elif item == "hoop":
        score = 9.450 + 9.350
    if item == "rope":
        score = 9.700 + 9.150

diff = abs(score - 20)
diff_percent = diff / 20 * 100

print(f"The team of {country} get {score:.3f} on {item}.")
print(f"{diff_percent:.2f}%")