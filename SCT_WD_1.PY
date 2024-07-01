def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the appropriate shift based on mode (encryption or decryption)
            if mode == 'encrypt':
                shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            elif mode == 'decrypt':
                shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('a' if char.islower() else 'A'))
            else:
                raise ValueError("Mode must be 'encrypt' or 'decrypt'.")
            result += shifted_char
        else:
            result += char  # If the character is not a letter, append it unchanged
    return result

def main():
    try:
        message = input("Enter your message: ").strip()
        shift = int(input("Enter the shift value (a positive integer): ").strip())
        mode = input("Enter 'encrypt' for encryption or 'decrypt' for decryption: ").strip().lower()

        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
            return

        encrypted_message = caesar_cipher(message, shift, mode)
        
        if mode == 'encrypt':
            print(f"Encrypted message: {encrypted_message}")
        elif mode == 'decrypt':
            print(f"Decrypted message: {encrypted_message}")
    
    except ValueError:
        print("Shift value must be a positive integer.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
