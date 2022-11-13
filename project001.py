print("WELCOME TO FIZZBUZZ GAMEE")
print("===========================")
n = int(input("masukkan angka  "))

for x in range(1, n+1):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("FIZZ")
    elif x % 5 == 0:
        print("BUZZ")
        continue
    print(x)