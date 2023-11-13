# customer_banking
OSU module 3 challenge
cd_account.py
-- Uses Account.py to create a class called Account for storing balance and interest
-- calculates the interest rate using create_cd_account which passes balance, rate, and months
-- updates cd balance and returns cd_account.balance, cd_account_interest

savings_account.py
-- Uses the same methods as cd_account.py

customer_banking.py
-- imports cd_account.py and savings_account.py to use the funtions within
-- uses pos_number_validate function to request numeric data from the user that is > 0
-- takes the input data for balance, interest, and maturity and updates savings and cd info
-- prints out updated balance with commas and to two decimal places.