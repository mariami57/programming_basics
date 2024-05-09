num_1 = input()
num_2 = input()

for i in range(int(num_1[0]),int(num_2[0]) + 1):
    for j in range(int(num_1[1]),int(num_2[1]) + 1):
        for k in range(int(num_1[2]),int(num_2[2]) + 1):
            for l in range(int(num_1[3]),int(num_2[3]) + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f"{i}{j}{k}{l}", end=" ")