import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("Enter the length of the password: "))
    if length < 6:
        print("Password length should be at least 6 characters.")
        return

    use_words = input("Do you want to include specific words in your password? (yes/no): ").lower()
    if use_words == "yes":
        words = input("Enter specific words separated by commas: ").split(',')
        password = ''.join(random.choice(words) for _ in range(length - len(words)))
        password += generate_random_password(len(words))
    else:
        password = generate_random_password(length)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    print("Your random password is:", password)

if __name__ == "__main__":
    main()
