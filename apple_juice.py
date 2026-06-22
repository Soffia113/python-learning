# 22.06.26

# Set the apple juice price to $2
apple_juice_price = 2.00

# Ask how much money the user has 
cash = float(input("How much money do you have? "))

# Print how much money the user has
print(f"You have ${cash}.")

#if, elif, and else statements as follow: 
if cash < apple_juice_price:
    print("You don't have enough money to buy apple juice")
    
else:
    answer = input("Would you like to buy apple juice (Y/N)? ").strip().upper()
    if answer == "N":
        print("No apple juice for you!")
    elif answer == "Y":
        print("Here is your apple juice. Enjoy!")
    else:
        print("Please enter Y or N.")
