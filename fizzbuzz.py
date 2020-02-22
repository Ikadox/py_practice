# 0~49で判定
for n in range(50):
    if 0 == n%15 :
        print("FizzBuzz")
    elif 0 == n%3 :
        print("Fizz")
    elif 0 == n%5 :
        print("Buzz")
    else :
        print(n)
