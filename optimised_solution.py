# Optimised solution: 6k +/- 1 primality test, early stopping once a value exceeds N,
# and a 'seen' set so no number is checked twice

import time

def is_prime(n):
    if n < 2:
        return False #returning False for the numbers less than 2
    if n in (2,3):
        return True #returning  True for the numbers 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False #returning False  for the numbers that are divisible by 2 or 3
    for i in range (5, int(n ** 0.5) + 1,6):
        if n % i == 0 or n % (i+2) == 0:
            return False #using a loop to check divisibility y numbers of form 6k+1 or 6k-1
    return True





def extract_primes(binary_str, N): #checking and validating that the input is binary (containing '0's and '1's)
    if not all(x == "0" or x == "1" for x in binary_str):
        return "0: INVALID BINARY STRING"

#creating sets for storing unique prime numbers and processed numbers
    unique_primes = set()
    length = len(binary_str)
    seen = set()

    for i in range(length):
        for j in range(i + 1, length + 1):
            # converting binary substrings to decimal numbers
            decimal_value = int(binary_str[i:j] , 2)
            # stopping if the number is greater than the N
            if decimal_value > N:
                break
            #skipping already processed prime numbers
            if decimal_value in unique_primes or decimal_value in seen:
                continue
            # adding the number to unique_primes set, otherwise adding it in seen
            if is_prime(decimal_value):
                unique_primes.add(decimal_value)
            else:
                seen.add(decimal_value)


    sorted_p = sorted(unique_primes) #sorting the prime numbers found
    all_p = len(sorted_p)
    print(f"{all_p}: ", end="")
    #if the prime numbers are less than 6, it returns them all. otherwise, only the first 3 and last 3
    if all_p < 6:
        return sorted_p
    else:
        return sorted_p[:3] +  sorted_p[-3:]



test_cases = [
    ("0100001101001111" , 999999), #output: 15: [2, 3, 5, 269, 2153, 17231] , 0.000072 seconds
    ("01000011010011110100110101010000" , 999999), #output: 28: [2, 3, 5, 10729, 17231, 85837] , 0.000160 seconds
    ("1111111111111111111111111111111111111111" , 999999), #output: 7: [3, 7, 31, 8191, 131071, 524287] , 0.000121 seconds
    ("010000110100111101001101010100000011000100111000" , 999999999), #output: 44: [2, 3, 5, 5571347, 41577089, 55398449] , 0.000679 seconds
    ("01000011010011110100110101010000001100010011100000110001" , 123456789012), #output: 52: [2, 3, 5, 84087683, 3920234023, 5625434161] , 0.003537 seconds
    ("0100001101001111010011010101000000110001001110000011000100111001" , 123456789012345), #output: 64: [2, 3, 5, 2724796139969, 5841981288761, 45810224399911] , 0.119735 seconds
    ("010000110100111101001101010100000011000100111000001100010011100100100001" , 123456789012345678), #output: 71: [2, 3, 5, 45810224399911, 7435453988964809, 18946016916092977] , 2.386161 seconds
    ("01000011010011110100110101010000001100010011100000110001001110010010000101000001" , 1234567890123456789), #output: 76: [2, 3, 5, 45810224399911, 7435453988964809, 18946016916092977] , 3.360558 seconds
    ("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100" , 1234567890123456789), #output: 81: [2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661] , 8.674471 seconds
    ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011" , 12345678901234567890) #output: 89: [2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661] , 11.170241 seconds
]

#calculating the execution time for each test case
for index, (binary_str, N) in enumerate(test_cases, start = 1):
    start = time.time()
    print(f"Test Case {index}:")
    print(extract_primes(binary_str, N))
    print("Execution time: ", end="")
    print(time.time() - start)
