# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account


# Validate entries as numbers
def pos_number_validate(prompt_message):
    while True:
        user_input = input(prompt_message)
        # if user enters "-" to denote a negative number, isdigit() will return false
        if user_input.replace('.','').isdigit():
            user_input = float(user_input)
            # print(f'You entered {user_input}.')
            break
        else:
            print("You must enter a valid positive number.")
    return user_input

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # Prompt for the savings balance > 0
    savings_balance = pos_number_validate("Please specify the savings balance to begin with: ")

    # Prompt for the interest rate > 0
    savings_interest = pos_number_validate("Please specify the interest rate to use: ")

    # Prompt for months > 0
    savings_maturity = int(pos_number_validate("Please specify the number of months: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f'Interest earned: {interest_earned:,.2f}.\nUpdated savings balance: {updated_savings_balance:,.2f}.')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # Prompt for the CD balance > 0
    cd_balance = pos_number_validate("Please specify the CD balance to begin with: ")

    # Prompt for the interest rate > 0
    cd_interest = pos_number_validate("Please specify the CD interest rate to use: ")

    # Prompt for months > 0
    cd_maturity = int(pos_number_validate("Please specify the number of months for maturity: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f'Interest earned: {interest_earned:,.2f}.\nUpdated CD balance: {updated_cd_balance:,.2f}.')

if __name__ == "__main__":
    # Call the main function.
    main()