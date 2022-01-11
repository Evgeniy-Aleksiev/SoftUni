for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except Exception as e:
        print("Error code:", e)

for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)