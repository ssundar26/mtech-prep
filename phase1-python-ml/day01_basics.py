# Day 1 - Python fundamentals
# Author: Satya Sundar
# Data: May 1, 2026

# --- Function 1: Basic greeting ------------------
def greet(name):
    """Return a personalized greeting string."""
    return f"Hello, {name}! Welcome to the 100-day-plan."

# --- Function 2: Arithmetic ----------------------
def add(a,b): 
    """Return the sum of two numbers."""
    return a + b

# --- Function 3: Prime check ---------------------
def is_prime(n):
    """Return true if n is a prime number, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n%i == 0:
            return False
        
# --- Function 4: Fibonacci sequence -------------
def fibonacci(n):
    """Return a list of the first n Fibonacci numbers."""
    if n <= 0:
        return []
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]        

# --- Function 5: palindrome Check -----------------
def is_palindrome(text):
    """REturn True if text reads the same forwards and backwards."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

# ___ Function 6: Temperature converter _____________
def celcius_to_farenhit(celcius):
    """Convert Celcius to Farenhit."""
    return (celcius * 9 / 5) + 32

# ___ Function 7: Factorial
def factorial(n):
    """Return n! using recursion. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("Factorial is not defined in negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n-1)

# ___ Function 8: Vowel Counter _______________________
def count_vowels(text):
    """Return the count of vowels in text (case-insensitive)."""
    vowels = "asiouAEIOU"
    return sum(1 for char in text if char in vowels)

# ___ Run and print results __________________________
if __name__ == "__main__":
    print(greet("Satya"))
    print(f"add(7,3) = {add(7,3)}")
    print(f"is_prime(17) = {is_prime(17)}")
    print(f"is_prime(18) = {is_prime(18)}")
    print(f"isfibonacci(10) = {fibonacci(10)}")
    print(f"is_palindrome('racecar) = {is_palindrome('racecar')}")
    print(f"is_palindrome('hello') = {is_palindrome('hello')}")
    print(f"celcius_to_farenhit(100) = {celcius_to_farenhit(100)}")
    print(f"factorial(6) = {factorial(6)}")
    print(f"count_vowels('Satya Sundar') = {count_vowels('Satya Sundar')}")
