def interest(principal, rate, periods):
    '''Interest.
    3 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
def interest(principal, rate, periods):
#final
    simple_interest = principal * (rate* periods)

#final value
    final_value = simple_interest + principal
    return final_value

#input values
principal = int(input("Enter Principal Investments: "))
rate = float(input("Enter Investment Rate: "))
periods = int(input("Enter Investment Period: "))

#calculate and print total investment
total_investment = interest(principal, rate, periods)
int(print(f"Your final value for investment is : {total_investment:.2f}"))
