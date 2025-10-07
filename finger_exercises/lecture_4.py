N = int(input("Enter a number: "))

i = 0
while (i**3 < N):
    i += 1

if i**3 == N:
    print(f"The square root of {N} is {i}")
else:
    print("error")

