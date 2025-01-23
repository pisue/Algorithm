result = 0 
for i in range(3):
    t = input()
    if t != "Fizz" and t != "Buzz" and t != "FizzBuzz":
        add_num = 3-i
        result = int(t) + add_num
        break;

if result % 3 == 0 and result % 5 != 0:
    print("Fizz")
elif result % 5 == 0 and result % 3 != 0:
    print("Buzz")
elif result % 15 == 0:
    print("FizzBuzz")
else:
    print(result)
    