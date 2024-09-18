'''This program uses bisection method to find the squareroot of any given number.'''

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:       #no square root for negative numbers
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:       #if the number's not -ve, 0 or 1.
        low = 0
        high = max(1, square_target)
        root = None         #setting lower limit to 0, upper limit(high) to either 1 or the number itself depending on whether it's >1 or <1
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2         #finding the middle point of that interval and squaring that to compare it with the number

            if abs(square_mid - square_target) < tolerance:         #if the square is within the tolerance level then the loop is broken, root is returned.
                root = mid
                break

            elif square_mid < square_target:            #if square is lower than the square target, lower limit is set to the mid point of the previous interval
                low = mid
            else:
                high = mid

        if root is None:                #root not found
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root


N = 25
square_root_bisection(N)