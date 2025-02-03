def fun(name, age, weight):
    if age > 17 or weight >= 80:
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")

while True:
    info = input().split()  
    name = info[0]
    age = int(info[1])
    weight = int(info[2])

    if name == "#" and age == 0 and weight == 0:
        break  # 종료 조건

    fun(name, age, weight)