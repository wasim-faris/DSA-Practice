arr = [10, 20, 30, 20, 40]
target = 10

last_occ = -1
target = 20

for i in range(len(arr)):
    if arr[i]==target:
        last_occ = i

if last_occ !=-1:
    print(f"Last occurnce at {last_occ}")
else:
    print("Not found")