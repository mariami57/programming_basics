n_pencils = int(input())
n_markers = int(input())
litres_of_detergent = int(input())
discount = int(input())

pencils_total_cost = n_pencils * 5.8
markers_total_cost = n_markers * 7.2
detergent_total_cost = litres_of_detergent * 1.2

price_before_discount = pencils_total_cost + markers_total_cost + detergent_total_cost
price_after_discount = price_before_discount - (price_before_discount * (discount / 100))

print(price_after_discount)

