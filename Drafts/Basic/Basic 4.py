def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.

    This function calculates the body mass index (BMI) of a person
        given their weight and height.

    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)

    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].

    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
def body_mass_index(weight, height):
    # Convert weight from pounds to kilograms
    weight_kg = weight * 0.45359237

    # Convert height from feet and inches to meters
    height_m = (height[0] * 0.3048) + (height[1] * 0.0254)

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)

    return bmi

# Example usage
weight = float(input("Enter Weight in lbs:"))
height = [int(input("Enter foot component of height:")) , int(input("Enter inch component of height:"))]
bmi = body_mass_index(weight, height)
print("BMI:", bmi)
