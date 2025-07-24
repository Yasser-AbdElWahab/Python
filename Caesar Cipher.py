# Get user input
text = input("Enter the text to encrypt: ")

# Create an empty list to store encrypted characters
encrypted_chars = []

# Go through each character in the input text
for char in text:
    if 'A' <= char <= 'Z':
        # Shift uppercase letter and wrap them around
        shifted = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
        encrypted_chars.append(shifted)
    elif 'a' <= char <= 'z':
        # Shift lowercase letter and wrap them around
        shifted = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
        encrypted_chars.append(shifted)
    else:
        # Non-letter characters stays the same
        encrypted_chars.append(char)

# Put the list into a string
encrypted_text = ''.join(encrypted_chars)

# Print the result
print("Encrypted:", encrypted_text)