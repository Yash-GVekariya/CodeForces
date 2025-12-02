n = int(input())
arr = []
angle_arr = []
for i in range(0, n):
    arr.append(int(input()))
    angle_arr.append(180 * (arr[i] - 2))

for i in range(0, n):
    print(angle_arr[i])
