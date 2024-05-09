rent_room = int(input())

statuette_price = rent_room * 0.7
catering_cost = statuette_price * 0.85
sound = catering_cost * 0.5

total_cost = rent_room + statuette_price + catering_cost + sound

print(f"{total_cost:.2f}")