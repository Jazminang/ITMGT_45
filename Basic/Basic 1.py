def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def calculate_savings(gross_pay, tax_rate, expenses):
    # Calculate taxes
    taxes = gross_pay * (tax_rate / 100)

    # Calculate net pay after deducting taxes
    net_pay = gross_pay - taxes

    # Calculate savings after deducting expenses
    savings = net_pay - expenses

    return savings

# Input values
gross_pay = int(input("Enter gross pay: "))
tax_rate = float(input("Enter tax rate (in percentage): "))
expenses = int(input("Enter expenses: "))

# Calculate and print the savings
total_savings = calculate_savings(gross_pay, tax_rate, expenses)
int(print(f"Your total savings: ₱{total_savings:.2f}"))