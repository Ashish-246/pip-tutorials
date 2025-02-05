master = list(map(int, input("Enter space-separated integers: ").split()))

number = int(input("Enter the number: "))

new_list = [num for num in master if num < number]

print(f"Numbers smaller than {number}: {new_list}" if new_list else f"No numbers are smaller than {number}.")
