list_1 = list(map(int, input("Enter space-separated numbers for list 1: ").split()))
list_2 = list(map(int, input("Enter space-separated numbers for list 2: ").split()))

new_list = [num for num in list_1 if num in list_2]

print("Common elements:", new_list if new_list else "No common elements found.")
