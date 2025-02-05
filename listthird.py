list = list(map(int, input("Enter space-separated integers: ").split()))
list.sort()
print("The third largest number in the list is:", list[-3])
