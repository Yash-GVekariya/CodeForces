h = int(input())
m = int(input())
s = int(input())
zone = input()

total_seconds = s + 60*m + 3600*h

if zone == 'AM':
    print(total_seconds)
elif zone == 'PM':
    print(total_seconds + 12*3600)