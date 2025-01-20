number = float(input("Enter a number: "))

if number <= 0:
    print("Invalid input")
    exit()

guess = number 
tolerance = 0.0001

while True:
    root = 0.5 * (guess + number / guess)
    if abs(root - guess) < tolerance:
        break
    guess = root

print(f"The square root of {number} is approximately: {root:.4f}")
