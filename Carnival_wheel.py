def main():
    n = int(input())
    data_arr = []
    for i in range(n):
        x, y, z = input().strip().split(' ')
        data_arr.append([int(x), int(y), int(z)])

    for i in range(n):
        print(data_arr)
        print(get_the_prize(data_arr))

def get_the_prize(data_arr):
    for [l, a, b] in data_arr:
        arr = []
        arr.append(a)
        for i in range(l - 1):
            if round((a + (i+1)*b) % l) == a:
                print(arr)
                return 0
            
        arr.append(round((a + (i+1)*b) % l))
    print(arr)
    return max(arr)
    
main()