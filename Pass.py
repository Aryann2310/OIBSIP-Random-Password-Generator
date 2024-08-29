import random
import string

def generate(length,pass_set):
  password = ''
  for _ in range(length):
    password += random.choice(pass_set)
  return password

def user_input():
  length = int(input("Enter password length: "))
  pass_set = ''
  if input("Include uppercase letters? (y/n): ").lower() == 'y':
    pass_set += string.ascii_uppercase
  if input("Include lowercase letters? (y/n): ").lower() == 'y':
    pass_set += string.ascii_lowercase
  if input("Include numbers? (y/n): ").lower() == 'y':
    pass_set += string.digits
  if input("Include symbols? (y/n): ").lower() == 'y':
    pass_set += string.punctuation
  return length, pass_set

def main():
  length, pass_set = user_input()
  if not pass_set:
    print("You must select at least one character set.")
    return
  password = generate(length, pass_set)
  print("Generated password: ", password)

if __name__ == "__main__":
  main()
