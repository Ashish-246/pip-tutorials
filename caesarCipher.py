def caesar_cipher(text, key, mode='encrypt'):
    """
    Encrypts or decrypts a message using the Caesar Cipher.

    Args:
        text: The message to be encrypted or decrypted.
        key: The shift value for the cipher.
        mode: 'encrypt' for encryption, 'decrypt' for decryption (default: 'encrypt').

    Returns:
        The encrypted or decrypted message.
    """
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

# Get input from the user
text = input("Enter a string: ")
key = int(input("Enter the code: "))

# Choose encryption or decryption
mode = input("Choose your option (encrypt/decrypt): ").lower() 
if mode not in ['encrypt', 'decrypt']:
    print("Invalid option!")
    exit()

# Perform the operation
result = caesar_cipher(text, key, mode)

# Print the result
print(f"{mode.capitalize()}ed Message:", result)