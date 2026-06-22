# 21.06.2

# Ask for user's name
name = input("What's your name? ").strip().title()

# Say hello to user
print(f"Hello, {name}")

# Ask for user's age
age = int(input("How old are you? "))

# Say user's age
print(f"You are {age} years old.")

# Add 5 years to user's age
print(f"In 5 years you'll be {age + 5}.")

# Ask user's favorite color
favorite_color = input("What's your favorite color? ").strip().lower()

print(f"Your name is {name}, you are {age} years old, and your favorite color is {favorite_color}.")