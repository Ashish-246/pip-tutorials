num_list = list(map(int, input("Enter space-separated integers: ").split()))

even_list = sorted([num for num in num_list if num % 2 == 0])

if even_list:
    print("Sorted list of even numbers:", even_list)
else:
    print("No even numbers found.")
