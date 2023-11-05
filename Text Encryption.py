def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def encrypt_message():
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value (0-25): "))

    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)

def decrypt_message():
    message = input("Enter the message to decrypt: ")
    shift = int(input("Enter the shift value (0-25): ") )

    decrypted_message = caesar_cipher(message, -shift)
    print("Decrypted message:", decrypted_message)

def main():
    while True:
        print("\nCaesar Cipher Application")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            encrypt_message()
        elif choice == '2':
            decrypt_message()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
