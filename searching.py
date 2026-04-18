
n = int(input("Enter how many elements you want in the list: "))
arr = []
print("Enter", n, "elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element you want to search: "))
found = False
for i in range(n):
    if arr[i] == key:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found in the list.")
