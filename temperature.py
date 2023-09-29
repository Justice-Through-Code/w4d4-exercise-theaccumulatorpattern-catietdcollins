
'''
    You are given a list of temperature readings in Celsius for a week. Your task is to implement a function that calculates and returns the average temperature for the week. To achieve this, you will use the accumulator pattern to accumulate the sum of temperatures and then calculate the average.

    Input

    A list temperatures containing n floating-point numbers representing the temperature readings for the week.
    (1 <= n <= 7, -20 <= temperatures[i] <= 40)
    
    Input Example
    temperatures = [20.5, 22.0, 18.5, 25.5, 26.0, 23.5, 19.0]  

    Output

    A single floating-point number representing the calculated average temperature.
    Example Output
    22.357142857142858


'''
##### ---------------------  Worked with Husayn, Myles, and Ras

from typing import List


def calculate_average_temperature(temperatures: List[float]) -> float:    
  
    num_temp = len(temperatures)
    if num_temp == 0:
        return None
    temper = 0
    
    # 1.1 TODO: # Initialize an accumulator variable to keep track of the sum of temperatures    
    # 1.2 TODO:# Iterate through the `temperatures` list, updating the accumulator with the current temperature.
    # 1.3 TODO: # Calculate and return the average temperature using the accumulated sum and the total number of readings.
    # 1.3 TODO: return the average temperature    
      
    for temp in temperatures:
        temper += temp
        avg_temp = temper / num_temp
    return avg_temp


temperatures = [20.5, 22.0, 18.5, 25.5, 26.0, 23.5, 19.0] 
    
average_temps = calculate_average_temperature(temperatures)

