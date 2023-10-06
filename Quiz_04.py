var = int(input("몇 단까지 출력할까요?"))

print("구구단을 출력합니다.")
def number(var):
    for a in range(1, var + 1):
        print("-------[" +str(a) + "단]-------")
        for b in range(1, var + 1):
             print(a, "X", b, "=", a*b)

number(var)
