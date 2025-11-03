def find_factors(num):
    # factors = {}            
    factors = []

    # for i in range(1, num):   
    for i in range(1, num + 1):
        # if num % i != 0:      
        if num % i == 0:
            # factors.add(i)    
            factors.append(i)

    return factors

print(find_factors(num=36))