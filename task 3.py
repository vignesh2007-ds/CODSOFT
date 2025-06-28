import random
import string

def generate_password():
    print("\n🔐 Password Generator")

    try:
        length = int(input("Enter desired password length: "))

        if length < 4:
            print("❗ Password length should be at least 4 for complexity.")
            return

        # Character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Combine all characters
        all_chars = lowercase + uppercase + digits + symbols

        # Ensure at least one character from each type
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
        ]

        # Fill the rest of the password length
        password += random.choices(all_chars, k=length - 4)

        # Shuffle the result to avoid predictable order
        random.shuffle(password)

        # Convert list to string
        final_password = ''.join(password)
        print(f"\n✅ Generated Password: {final_password}")

    except ValueError:
        print("❗ Invalid input. Please enter a number.")

# Run the generator
generate_password()
