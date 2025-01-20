def caesar_cipher(text, key, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord(char) + (key if mode == 'encrypt' else -key)
            if char.isupper():
                shift = (shift - ord('A')) % 26 + ord('A')
            else:
                shift = (shift - ord('a')) % 26 + ord('a')
            result += chr(shift)
        else:
            result += char
    return result

text = input("Enter a string: ")
key = int(input("Enter the code: "))
mode = input("Choose your option (encrypt/decrypt): ").lower() 

if mode not in ['encrypt', 'decrypt']:
    print("Invalid option!")
else:
    result = caesar_cipher(text, key, mode)
    print(f"{mode.capitalize()}ed Message:", result)
