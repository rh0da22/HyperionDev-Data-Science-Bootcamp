import math

while True:
    print("\n Investment - to calculate the amount of interest you'll earn on your investment")
    print("\n Bond - to calculate the amount you'll have to pay on a home loan")

    # The user can enter either investment or bond. The answer will be case insensitive.
    answer = input("\n Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    while answer not in ["investment", "bond"]:
        print("Sorry, I don't recognise your response. Please enter either 'investment' or 'bond'.")
        answer = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    # This does the investment calculation based on the user's choice.
    if answer == "investment":
        # We collect the details needed to do the calculation.
        principal = float(input("\n Enter the amount you want to deposit in £: "))
        ir = float(input("Enter the interest rate: "))
        years = int(input("Enter the number of years you plan to invest for: "))
        interest_type = input("Do you want 'simple' or 'compound' interest?: ").lower()

    # The calculation is worked out based on the interest type then displayed. An error message is printed if an invalid interest type is entered.
        if interest_type == "simple":
            interest = principal*(1+((ir/100)*years))
    
        elif interest_type == "compound":
            interest = principal*math.pow((1+(ir/100)), years)
        else:
            print("\n Sorry I dont recognise your response.")
    
        print(f"\n With an interest rate of {ir}%, you will get £{interest:.2f} in total after {years} years.")

    # This works out the calculation for a bond if it is selected. The monthly repayments are then displayed. An error message is printed if an invalid interest type is entered.
    elif answer == "bond":
    # We collect the details needed to do the calculation.
        house_value = float(input("\n Enter thr present value of the house in £: "))
        ir = float(input(" Enter the interest rate: "))
        months = int(input(" Enter the number of months you plan to take to repay: "))
        monthly_ir = (ir/100)/12
        repayment = (monthly_ir*house_value)/(1-((1+monthly_ir)**(-months)))

        print(f"\n You will have to repay £{repayment:.2f} each month.")

    else:
        print("\n Sorry, I don't recognise your response. Please try again.")
        continue

    print("-" * 60) 

    another = input("Would you like to do another bond or investment calculation? Enter Yes or No: ").lower()
    if another != "yes":
        break
