print("semenov_igor")
print("20kis3")
print ("sleepy")

n = int(input("enter the number: "))

f1 = 1
f2 = 1
fs = 0

n = int(n)

i = 0
while i < n - 2:
    fs = f1 + f2
    f1 = f2
    f2 = fs
    i = i + 1

print(f2)
