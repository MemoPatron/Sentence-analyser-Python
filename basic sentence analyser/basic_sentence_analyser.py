#Write a Python program that accepts a sentence as input and returns the number of letters and digits in the sentence. 
#For example, if the input is “Hello World! 123”, the output should be “Letters: 10, Digits: 3”.

print("Write a sentence, and I will calculate how many characters and numbers there are")
print()

content = input("Your desired sentece: ")

alpha_count = 0
num_count = 0

for char in content:
  if char.isalpha():
    alpha_count += 1
  elif char.isdigit():
    num_count += 1

print("There are", alpha_count, "characters and", num_count, "numbers in your sentence.")





