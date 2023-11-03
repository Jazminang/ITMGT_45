def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def material_waste(total_material, material_units, num_jobs, job_consumption):
 #Multiply the number of jobs by the material consumption per job.
    total_material_consumed = num_jobs * job_consumption

    #Subtract the total material consumed from the total material available.
    waste = total_material-total_material_consumed
    return waste

# Input values
total_material = int(input("Enter total materials: "))
material_units= str(input("units of materials: "))
num_jobs = int(input("Enter number of jobs: "))
job_consumption = int(input("Enter job consumption: "))

# Calculate and print the savings
total_waste= material_waste(total_material, material_units, num_jobs, job_consumption)
str(print(f"Your total waste: {total_waste:.2f}{material_units}"))
