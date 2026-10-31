# Basic solution: checks every substring and tests primality by trial division up to sqrt(n)


import time #importing time for measuring the execution time

def is_prime(n):
    """
    defining a function to check if the number is prime or not
    all of the numbers less than 2 are not primes
    then looping from 2 to square root of n and if n is divisable by any number in this range, it's not prime
    if no factors were found, the number is prime (returning True)
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def extract_primes(binary_str, N):
    """
    defining a function to extract unique prime numbers from binary strings
    it checks if the input string is a binary string
    it checks if the input entered is containing only '0's and '1's
    if it is anything except 0s and 1s, it's returning 0 as no prime numbers and invalid binary string
    """

    for x in binary_str:
        if x != "0" and x != "1":
            return "0: INVALID BINARY STRING"


    unique_primes = set() #using a set to store unique prime numbers
    length = len(binary_str) #getting the length of binary string


    """
    it extracts substrings from index i to j and converts them to decimal numbers
    then it checks whether that decimal value is smaller than N we entered AND if it is a prime number
    if the conditions are correct, the decimal value is going to be added in the set  
    """

    for i in range(length):
        for j in range(i + 1, length + 1):
            decimal_value = int(binary_str[i:j], 2)
            if decimal_value < N and is_prime(decimal_value):
                unique_primes.add(decimal_value)

    sorted_p = sorted(unique_primes) #sorting the prime numbers
    all_p = len(sorted_p) #counting total number of unique prime numbers found

    print(f"{all_p}: ", end="")
    if all_p < 6:
        # if the total number of unique prime numbers are fewer than 6, it is going to return all of them
        return sorted_p
    #otherwise, it is going to return first 3 and last 3 primes
    else:
        return sorted_p[:3] + sorted_p[-3:]

#testing the code with all of the test cases given
test_cases = [
    ("1010110101" , 1000),
    ("0100001101001111" , 999999), #output = 15: [2, 3, 5, 269, 2153, 17231] , 0.000091 seconds
    ("01000011010011110100110101010000" , 999999), #output = 28: [2, 3, 5, 10729, 17231, 85837] , 0.000327 seconds
    ("1111111111111111111111111111111111111111" , 999999), #output = 7: [3, 7, 31, 8191, 131071, 524287] , 0.001041 seconds
    ("010000110100111101001101010100000011000100111000" , 999999999), #44: [2, 3, 5, 5571347, 41577089, 55398449] , 0.002062 seconds
    ("01000011010011110100110101010000001100010011100000110001" , 123456789012), #52: [2, 3, 5, 84087683, 3920234023, 5625434161] , 0.011347 seconds
    ("0100001101001111010011010101000000110001001110000011000100111001" , 123456789012345), #64: [2, 3, 5, 2724796139969, 5841981288761, 45810224399911] , 0.439126 seconds
    ("010000110100111101001101010100000011000100111000001100010011100100100001" , 123456789012345678), #71: [2, 3, 5, 45810224399911, 7435453988964809, 18946016916092977] , 14.249011 seconds
    ("01000011010011110100110101010000001100010011100000110001001110010010000101000001" , 1234567890123456789), #76: [2, 3, 5, 45810224399911, 7435453988964809, 18946016916092977] , 17.563029 seconds
    ("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100" , 1234567890123456789), #81: [2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661] , 55.792771 seconds
    ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011" , 12345678901234567890) #89: [2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661] , 103.205363. seconds
]


for index, (binary_str, N) in enumerate(test_cases, start = 1):

    start = time.time() #starting time measurement
    print(f"Test Case {index}:")
    print(extract_primes(binary_str, N))
    print("Execution time: ", end="")
    print(time.time() - start) #print execution time

