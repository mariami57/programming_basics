n_breads = int(input())
n_eggs = int(input())
n_cookies = int(input())

colouring_price = n_eggs * 12 * 0.15
total_cost = (n_breads * 3.2) + (n_eggs * 4.35) + colouring_price + (n_cookies * 5.4)

print(f"{total_cost:.2f}")