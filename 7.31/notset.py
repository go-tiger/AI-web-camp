arr1 = [1, 2, 3, 4, 5, 2, 6, 7, 1, 8, 9, 10, 4, 8]

arr2 = []

for i in arr1:
    if i not in arr2:
        arr2.append(i)

print(arr2)