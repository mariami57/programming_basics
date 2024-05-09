num1_upper = int(input())
num2_upper = int(input())
num3_upper = int(input())
counter = 0
prime_number = False
for n1 in range(1,num1_upper+1):
    for n2 in range(2,num2_upper+1):
        counter = 0
        for number in range(1,n2+1):
            if n2 % number == 0:
                counter += 1
            if counter == 2:
                prime_number = True
            else:
                prime_number = False
        for n3 in range(1,num3_upper+1):
            if n1 % 2 == 0 and prime_number and n3 % 2 == 0:
                print(f"{n1} {n2} {n3}")
