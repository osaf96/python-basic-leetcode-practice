# Two crystal ball problem
# URL: https://open.kattis.com/problems/twocrystalball
# Date: 2021-07-29

 


def two_crystal_balls(breaks):
    n = len(breaks)
    interval = int(n**0.5)  # Step size

    # First crystal ball: Find the interval where it breaks
    for i in range(interval, n, interval):
        if breaks[i]:
            break
        else:
            i = n  # In case the first ball didn't break in the intervals

    # Determine the start of the interval
    start = i - interval

    # Second crystal ball: Find the exact floor in the interval
    for j in range(start, min(i, n)):
        if breaks[j]:
            return j

    return -1  # Return -1 if no breaking point is found

# Test the function
floors = 100
break_point = 73
breaks = [False] * break_point + [True] * (floors - break_point)

# result = two_crystal_balls(breaks)
# print(f"The highest safe floor is: {result}")

# Need to practice
 